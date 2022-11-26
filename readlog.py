#!/usr/bin/env python3
import pandas as pd
import re
import sys
from collections import Counter
from dataclasses import dataclass
from typing import Union


# Initial log filters
CLOSED_LOOP = 1  # Closed loop enabled is 1. Closed loop disabled is 0.
ACC_POS = 25  # In percent

# Monitor condition variables
FK_TRESHOLD = -2  # In degrees. The more negative, the more timing retarded.
FKL_THRESHOLD = -2  # In degrees. The more negative, the more timing retarded.
DAM_TRESHOLD = 1
OIL_TEMP_TRESHOLD = 250  # In Fahrenheit

        
def load_csv(file: str) -> pd.DataFrame:
    df = pd.read_csv(file, encoding = "ISO-8859-1")
    return df


def apply_global_filters(df: pd.DataFrame, monitors) -> pd.DataFrame:
    df_filtered = df[df[monitors.acc_pos] > ACC_POS]
   # df_filtered = df[df[monitors.closed_loop] == CLOSED_LOOP]
    return df_filtered

    
def verify_log_monitors(df: pd.DataFrame) -> list:
    df_columns = df.columns.to_list()
    monitor_list = (
            # Monitors shared across all Subarus
            'AF Sens 1 Ratio (AFR)',
            'Comm Fuel Final (AFR)',
            'AF Correction 1 (%)',
            'AF Learning 1 (%)',
            'Oil Temp (F)',
            
            # VA platform specific monitor names
            'Accel. Position (%)', 
            'Feedback Knock (°)', 
            'Fine Knock Learn (°)', 
            'Dyn. Adv. Mult (DAM)', 
            'Roughness Cyl 1 (count)', 
            'Roughness Cyl 2 (count)', 
            'Roughness Cyl 3 (count)', 
            'Roughness Cyl 4 (count)', 
            'Closed Loop Sw. (on/off)',
            
            # VB platform specific monitor names
            'Accel Position (%)',
            'Feedback Knock (degrees)',
            'Fine Knock Learn (degrees)',    
            'Dyn Adv Mult (value)',
            'Roughness Cyl 1 (misfire count)',
            'Roughness Cyl 2 (misfire count)',
            'Roughness Cyl 3 (misfire count)',
            'Roughness Cyl 4 (misfire count)',
            'Closed Loop Sw (status)',
    )
    monitors = [x for x in monitor_list if x in df_columns]
    return monitors


@dataclass
class Monitors:
    af_ratio: str
    af_comm: str
    af_corr: str
    af_learn: str
    oil_temp: str
    acc_pos: str
    fk: str
    fkl: str
    dam: str
    cyl1_rough: str
    cyl2_rough: str
    cyl3_rough: str
    cyl4_rough: str
    closed_loop: str

    
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
        cyl1 = self.df[self.mon.cyl1_rough].to_list()
        mf1 = True if any(item > 0 for item in cyl1) else False
        cyl2 = self.df[self.mon.cyl2_rough].to_list()
        mf2 = True if any(item > 0 for item in cyl2) else False
        cyl3 = self.df[self.mon.cyl3_rough].to_list()
        mf3 = True if any(item > 0 for item in cyl3) else False
        cyl4 = self.df[self.mon.cyl4_rough].to_list()
        mf4 = True if any(item > 0 for item in cyl4) else False
        return mf1, mf2, mf3, mf4

    def af_correct_exceed(self) -> bool:
        self.df['AF Actual Correction (%)'] = self.df[self.mon.af_corr] + self.df[self.mon.af_learn]
        af_actual = self.df['AF Actual Correction (%)'].to_list()
        af_exceeded = False
        if any(item > 18 for item in af_actual):
            af_exceeded = True
        elif any(item < -18 for item in af_actual):
            af_exceeded = True
        else:
            return af_exceeded

    def feedback_knock(self) -> Union[bool,Counter]:
        fk = self.df[self.mon.fk].to_list()
        fk_count = Counter(fk) if all(item < FK_TRESHOLD for item in fk) else None
        return fk_count

    def fineknock_learn(self) -> Union[bool,Counter]:
        fkl = self.df[self.mon.fkl].to_list()
        fkl_count = Counter(fkl) if all(item < FKL_THRESHOLD for item in fkl) else None
        return fkl_count

    def dam_exceed(self) -> Union[bool,Counter]:
        dam_list = self.df[self.mon.dam].to_list()
        end_dam = Counter(dam_list) if dam_list[-1] < DAM_TRESHOLD else None
        return end_dam
    
    def oil_temp_exceed(self) -> bool:
        oil_temps = self.df[self.mon.oil_temp].to_list()
        oil_temp_exceeded = True if any(item >= OIL_TEMP_TRESHOLD for item in oil_temps) else False
        return oil_temp_exceeded


def main() -> None:
    # file = sys.argv[1]
    df = load_csv('datalog20.csv')
    verified_monitors = verify_log_monitors(df)
    monitors = Monitors(*verified_monitors)
    df = apply_global_filters(df, monitors)
    conditions = MonitorConditions(df, monitors)
    
    for status in conditions.status_cyl_misfire: 
        if status: print('Misfire detected')
    if conditions.status_fk: print('Feedback knock detected')
    if conditions.status_fkl: print('Fineknock Learn detected')
    if conditions.status_af_exceed: print('AF correction exceeded')
    if conditions.status_dam: print(f'DAM dropped below {DAM_TRESHOLD}')
    if conditions.status_oil_temp: print(f'Oil temp exceeded {OIL_TEMP_TRESHOLD}')

    
if __name__ == "__main__":
    main()