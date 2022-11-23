#!/usr/bin/env python3
import pandas as pd
import re
import sys
from collections import Counter
from typing import Union


class Log:
    def __init__(self, file):
        self.load_csv(file)

    def load_csv(self, file: str) -> None:
        self.df = pd.read_csv(file, encoding = "ISO-8859-1")
        self.monitors = self.df.columns
        self.log_info = self.get_log_info()
        self.car = self.id_car()
        self.define_monitors()
        # To remove noise in log, filter data when acc_pos > 25%.
        self.df = self.df[self.df[self.acc_pos] > 25] 

    def get_log_info(self) -> dict:
        info = self.df.iloc[:,-1:].to_string()
        info = re.findall(r'\[.*?\]', info)
        log_info = {}
        log_info['AP Version'] = info[0][1:-1]
        log_info['Car'] = info[1][1:-1]
        log_info['Tune'] = info[2][1:-1]
        return log_info
        
    def define_monitors(self) -> None:
        # The following monitors are shared across models
        self.af_ratio = 'AF Sens 1 Ratio (AFR)'
        self.af_com = 'Comm Fuel Final (AFR)'
        self.af_corr = 'AF Correction 1 (%)'
        self.af_learn = 'AF Learning 1 (%)'
        # The following monitors _ARE_NOT_ shared across models and need to be defined separately
        if 'wrx_va' in self.car:
            self.acc_pos = 'Accel. Position (%)'
            self.fk = 'Feedback Knock (°)'
            self.fkl = 'Fine Knock Learn (°)'
            self.dam = 'Dyn. Adv. Mult (DAM)'
            self.cyl1 = 'Roughness Cyl 1 (count)'
            self.cyl2 = 'Roughness Cyl 2 (count)'
            self.cyl3 = 'Roughness Cyl 3 (count)'
            self.cyl4 = 'Roughness Cyl 4 (count)'
        elif 'wrx_vb' in self.car:
            self.acc_pos = 'Accel Position (%)'
            self.fk = 'Feedback Knock (degrees)'
            self.fkl = 'Fine Knock Learn (degrees)'
            self.dam = 'Dyn Adv Mult (value)'
            self.cyl1 = 'Roughness Cyl 1 (misfire count)'
            self.cyl2 = 'Roughness Cyl 2 (misfire count)'
            self.cyl3 = 'Roughness Cyl 3 (misfire count)'
            self.cyl4 = 'Roughness Cyl 4 (misfire count)'
    
    def verify_monitors(self):
        # Check if defined monitors exist in data log.
        pass

    def boost_target(self):
        pass

    def cyl_misfire(self) -> tuple:
        cyl1 = self.df[self.cyl1].to_list()
        mf1 = True if any(item > 0 for item in cyl1) else False
        cyl2 = self.df[self.cyl2].to_list()
        mf2 = True if any(item > 0 for item in cyl2) else False
        cyl3 = self.df[self.cyl3].to_list()
        mf3 = True if any(item > 0 for item in cyl3) else False
        cyl4 = self.df[self.cyl4].to_list()
        mf4 = True if any(item > 0 for item in cyl4) else False
        return mf1, mf2, mf3, mf4

    def id_car(self) -> str:
        # va and vb models determined by car year.
        va_years = [2015, 2016, 2017, 2018, 2019, 2020, 2021]
        vb_years = [2022, 2023, 2024]
        year = int(self.log_info['Car'].split()[0])
        if year in va_years:
            car = 'wrx_va'
        elif year in vb_years:
            car = 'wrx_vb'
        else:
            print('Unable to determine car model from log.')
            sys.exit()
        return car

    def af_actual(self) -> bool:
        self.df['AF Actual Correction (%)'] = self.df[self.af_corr] + self.df[self.af_learn]
        af_actual = self.df['AF Actual Correction (%)'].to_list()
        af_exceeded = False
        if any(item > 18 for item in af_actual):
            af_exceeded = True
        elif any(item < -18 for item in af_actual):
            af_exceeded = True
        else:
            return af_exceeded

    def feedback_knock_count(self) -> Union[bool,Counter]:
        fk = self.df[self.fk].to_list()
        fk_count = Counter(fk) if all(item < -2 for item in fk) else None
        return fk_count

    def fineknock_learn_count(self) -> Union[bool,Counter]:
        fkl = self.df[self.fkl].to_list()
        fkl_count = Counter(fkl) if all(item < -2 for item in fkl) else None
        return fkl_count

    def end_log_dam(self) -> Union[bool,Counter]:
        dam_list = self.df[self.dam].to_list()
        end_dam = Counter(dam_list) if dam_list[-1] < 1 else None
        return end_dam

    def review(self) -> list:
        fk = self.feedback_knock_count()
        fkl = self.fineknock_learn_count()
        dam = self.end_log_dam()
        af = self.af_actual()
        mf = self.cyl_misfire()
        
        results = []
        results.append(self.car)
    
        if fk or fkl or dam is not None:
            results.append(f'DAM: {self.dam}\nFeedback Knock: {self.fk}\nFine Knock Learn: {self.fkl}')
        if af:
            results.append(f'AF correction exceeded threshold')
        if True in mf:  
            results.append(f'Engine misfire detected')
        else:
            results.append(f'No issues found')
        return results


if __name__ == "__main__":
    file = sys.argv[1]
    log = Log(file)
    output = log.review()
    for i in output:
        print(i)