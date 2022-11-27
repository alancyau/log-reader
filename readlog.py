#!/usr/bin/env python3
import pandas as pd
import sys
from collections import Counter
from dataclasses import dataclass
from typing import Union


# Initial log filters
VA_CLOSED_LOOP = 'on'
VB_CLOSED_LOOP = 1
ACC_POS = 25  # In percent

# Monitor condition variables
FK_TRESHOLD = -2  # In degrees. The more negative, the more timing retarded.
FKL_THRESHOLD = -2  # In degrees. The more negative, the more timing retarded.
DAM_TRESHOLD = 1
OIL_TEMP_TRESHOLD = 250  # In Fahrenheit
AF_CORRECT_POSITIVE_TRESHOLD = 18  # In percent
AF_CORRECT_NEGATIVE_TRESHOLD = -18  # In percent


def load_csv(file: str) -> pd.DataFrame:
    df = pd.read_csv(file, encoding = "ISO-8859-1")
    return df


def apply_global_filters(df: pd.DataFrame, monitors) -> pd.DataFrame:
    df_acc = df[df[monitors['acc_pos']] > ACC_POS]
    df_cl = df_acc[df_acc[monitors['closed_loop']] == VA_CLOSED_LOOP]
    if len(df_cl):
        return df_cl
    else: 
        df_cl = df_acc[df_acc[monitors['closed_loop']] == VB_CLOSED_LOOP]
        return df_cl

    
def verify_log_monitors(df: pd.DataFrame) -> dict:
    df_columns = df.columns.to_list()
    monitors = {
        'af_ratio': ['AF Sens 1 Ratio (AFR)'],
        'af_comm': ['Comm Fuel Final (AFR)'],
        'af_corr': ['AF Correction 1 (%)'],
        'af_learn': ['AF Learning 1 (%)'],
        'oil_temp': ['Oil Temp (F)'],
        'acc_pos': ['Accel. Position (%)', 'Accel Position (%)'],
        'fk': ['Feedback Knock (°)', 'Feedback Knock (degrees)'],
        'fkl': ['Fine Knock Learn (°)', 'Fine Knock Learn (degrees)'],
        'dam': ['Dyn. Adv. Mult (DAM)', 'Dyn Adv Mult (value)'],
        'cyl1_rough': ['Roughness Cyl 1 (count)', 'Roughness Cyl 1 (misfire count)'],
        'cyl2_rough': ['Roughness Cyl 2 (count)', 'Roughness Cyl 2 (misfire count)'],
        'cyl3_rough': ['Roughness Cyl 3 (count)', 'Roughness Cyl 3 (misfire count)'],
        'cyl4_rough': ['Roughness Cyl 4 (count)', 'Roughness Cyl 4 (misfire count)'],
        'closed_loop': ['Closed Loop Sw. (on/off)', 'Closed Loop Sw (status)'],
}
    for k in monitors:
        for item in monitors[k]:
            if item in df_columns:
                monitors[k] = item
    return monitors


class MonitorConditions:
    def __init__(self, df: pd.DataFrame, monitors) -> None:
        self.df = df
        self.mon = monitors
        self.status_cyl_misfire = self.cylinder_misfire()
        self.status_af_exceed = self.af_correct_exceed()
        self.status_fk = self.feedback_knock()
        self.status_fkl = self.fineknock_learn()
        self.status_dam = self.dam_exceed()
        self.status_oil_temp = self.oil_temp_exceed()

    def af_command_vs_actual(self):
        pass

    def boost_command_vs_actual(self):
        pass

    def cylinder_misfire(self) -> tuple:
        cyl1 = self.df[self.mon['cyl1_rough']].to_list()
        mf1 = True if any(item > 0 for item in cyl1) else False
        cyl2 = self.df[self.mon['cyl2_rough']].to_list()
        mf2 = True if any(item > 0 for item in cyl2) else False
        cyl3 = self.df[self.mon['cyl3_rough']].to_list()
        mf3 = True if any(item > 0 for item in cyl3) else False
        cyl4 = self.df[self.mon['cyl4_rough']].to_list()
        mf4 = True if any(item > 0 for item in cyl4) else False
        return mf1, mf2, mf3, mf4

    def af_correct_exceed(self) -> bool:
        self.df['AF Actual Correction (%)'] = self.df[self.mon['af_corr']] + self.df[self.mon['af_learn']]
        af_actual = self.df['AF Actual Correction (%)'].to_list()
        if any(item > AF_CORRECT_POSITIVE_TRESHOLD for item in af_actual):
            return True
        elif any(item < AF_CORRECT_NEGATIVE_TRESHOLD for item in af_actual):
            return True
        else:
            return False

    def feedback_knock(self) -> Union[bool,Counter]:
        fk = self.df[self.mon['fk']].to_list()
        return Counter(fk) if any(item < FK_TRESHOLD for item in fk) else None

    def fineknock_learn(self) -> Union[bool,Counter]:
        fkl = self.df[self.mon['fkl']].to_list()
        return Counter(fkl) if any(item < FKL_THRESHOLD for item in fkl) else None

    def dam_exceed(self) -> bool:
        dam_list = self.df[self.mon['dam']].to_list()
        return True if dam_list[-1] < DAM_TRESHOLD else False
    
    def oil_temp_exceed(self) -> bool:
        oil_temps = self.df[self.mon['oil_temp']].to_list()
        return True if any(item >= OIL_TEMP_TRESHOLD for item in oil_temps) else False


def main() -> None:
    #file = sys.argv[1]
    df = load_csv('22.csv')
    verified_monitors = verify_log_monitors(df)
    df = apply_global_filters(df, verified_monitors)
    conditions = MonitorConditions(df, verified_monitors)
    
    for status in conditions.status_cyl_misfire: 
        if status: print('Misfire detected')
    if conditions.status_fk: print(f'Feedback knock detected\n{conditions.status_fk}')
    if conditions.status_fkl: print(f'Fineknock learn detechted\n{conditions.status_fkl}')
    if conditions.status_af_exceed: print('AF correction exceeded')
    if conditions.status_dam: print(f'Ending drive DAM dropped below {DAM_TRESHOLD}')
    if conditions.status_oil_temp: print(f'Oil temp exceeded {OIL_TEMP_TRESHOLD}')

    
if __name__ == "__main__":
    main()