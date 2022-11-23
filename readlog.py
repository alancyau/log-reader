#!/usr/bin/env python3
from collections import Counter
import pandas as pd
import sys


class Log:
    def __init__(self, df):
        self.df = df
        self.filter_accel_pos()

    def carid(self):
        va = (2015, 2016, 2017, 2018, 2019, 2020, 2021)
        vb = (2022, 2023, 2024)
        year = self.df.iloc[:,-1:].to_string().split('[')
        for i in year[3]:
            print(i)

    def af_correction(self):
        pass

    def af_learn(self):
        pass

    def af_ratio(self):
        pass

    def filter_accel_pos(self):
        self.df = self.df[self.df['Accel Position (%)'] > 25]
        
    def feedback_knock(self):
        fk = self.df['Feedback Knock (degrees)'].to_list()
        if all(item < -2 for item in fk):
            self.fk = Counter(fk)
        else:
            self.fk = False

    def fineknock_learn(self):
        fkl = self.df['Fine Knock Learn (degrees)'].to_list()
        if all(item < -2 for item in fkl):
            self.fkl = Counter(fkl)
        else:
            self.fkl = False

    def dam(self):
        dam = self.df['Dyn Adv Mult (value)'].to_list()
        if all(item < 1 for item in dam):
            self.dam = Counter(dam)
        else:
            self.dam = False

    def review(self):
        self.feedback_knock()
        self.fineknock_learn()
        self.dam()
        self.carid()
        if self.fk or self.fkl or self.dam:
            print(f'DAM: {self.dam}\nFeedback Knock: {self.fk}\nFine Knock Learn: {self.fkl}')
        else:
            print(f'No issues found')


if __name__ == "__main__":
    #filename = sys.argv[1]
    filename = "22-wrx.csv"
    df = pd.read_csv(filename, encoding = "ISO-8859-1")
    log = Log(df)
    log.review()