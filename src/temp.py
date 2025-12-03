

import csv
import pandas as pd
import numpy as np
import os
import dateutil
import datetime

DATA_DIR = os.path.join('..','data')


def calculate_day_timedelta(dow):
    td = dow - 3
    if dow < 3:
        return 4 + dow
    
    return td


with open(os.path.join(DATA_DIR,'market_base_patterns.csv'), mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    capacity_week_plan = {}
    departure_week_cols = {}
    for i,row in enumerate(csv_reader):
        market = row[0]
        base = row[1]
        for j,col in enumerate(row):
            if j<=1:
                continue

            if i==0:
                departure_week = dateutil.parser.parse(col)
                capacity_week_plan[departure_week] = []
                departure_week_cols[j] = departure_week
            else:
                if not departure_week_cols[j] in capacity_week_plan:
                    capacity_week_plan[departure_week_cols[j]] = []
                capacity_week_plan[departure_week_cols[j]].append((base,market,col))
        
    capacity_plan = {}
    for k in capacity_week_plan.keys():
        departure_week = k
        for row in capacity_week_plan[k]:
            digits = str(row[2])
            for digit in digits:
                departure_date = departure_week + datetime.timedelta(days=calculate_day_timedelta(int(digit)))
        
                if not departure_date in capacity_plan:
                    capacity_plan[departure_date] = []
                
                r = [departure_week]
                r.extend(row)
                capacity_plan[departure_date].append(r)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        