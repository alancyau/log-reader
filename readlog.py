#!/usr/bin/env python3
from collections import Counter
import pandas as pd
import re
import sys
 

class Log:
    def __init__(self):
        self.df = None
        self.monitors = None
        self.ap_version = None
        self.car_model = None
        self.tune = None

    def load(self, file):
        self.df = pd.read_csv(file, encoding = "ISO-8859-1")
        self.df = self.df[self.df['Accel Position (%)'] > 25] 
        self.monitors = self.df.columns
        self.log_info()

    def verify_monitors(self):
        monitor_list = ('Accel Position (%)', 'Feedback Knock (degrees)', 'Fine Knock Learn (degrees)', 'Dyn Adv Mult (value)')
        missing_monitors = []
        for monitor in monitor_list:
            if monitor not in self.df.columns:
                missing_monitors.append(monitor)
        if missing_monitors:
            return False
        else:
            return True

    # need to fix regex
    def log_info(self):
        info = self.df.iloc[:,-1:].to_string()
        info = re.findall(r'\[.*?\]', info)
        self.ap_version = info[0]
        self.car_model = info[1]
        self.tune = info[2]

    def af_ratio(self):
        pass

    def af_target(self):
        pass
        
    def feedback_knock_count(self):
        fk = self.df['Feedback Knock (degrees)'].to_list()
        if all(item < -2 for item in fk):
            self.fk = Counter(fk)
        else:
            self.fk = None

    def fineknock_learn_count(self):
        fkl = self.df['Fine Knock Learn (degrees)'].to_list()
        if all(item < -2 for item in fkl):
            self.fkl = Counter(fkl)
        else:
            self.fkl = None

    def dam_count(self):
        dam = self.df['Dyn Adv Mult (value)'].to_list()
        if dam[-1] < 1:
            self.dam = Counter(dam)
        else:
            self.dam = None

    def review(self):
        if self.verify_monitors() is True:
            self.feedback_knock_count()
            self.fineknock_learn_count()
            self.dam_count()
        
        if self.fk or self.fkl or self.dam is not None:
            print(f'DAM: {self.dam}\nFeedback Knock: {self.fk}\nFine Knock Learn: {self.fkl}')
        else:
            print(f'No issues found')


if __name__ == "__main__":
    file = sys.argv[1]
    log = Log()
    log.load(file)
    log.review()
    