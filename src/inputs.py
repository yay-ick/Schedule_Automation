

import csv
import pandas as pd
import numpy as np
import os
import dateutil
import datetime

DATA_DIR = os.path.join('..','data')


def read_airports():
    with open(os.path.join(DATA_DIR,'airports.csv'), mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        airports = {}
        for row in csv_reader:
            airport = row[0]
            airports[airport] = {}
            airports[airport]['tz'] = 'CT'
            airports[airport]['lat'] = float(row[1])
            airports[airport]['lon'] = float(row[2])

    return airports

def read_station_constraints():
    with open(os.path.join(DATA_DIR,'station_constraints.csv'), mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        constraints = {}
        cols = {}
        for i,row in enumerate(csv_reader):
            if i>0:
                airport = row[0]
                constraints[airport] = {}
            for j,col in enumerate(row):
                if i==0: #header
                    cols[j] = col
                else:
                    if 'Latest' in cols[j] or 'Earliest' in cols[j]:
                        constraints[airport][cols[j]] = dateutil.parser.parse(col).time()
                    elif col!=airport:
                        constraints[airport][cols[j]] = float(col)

    return constraints


def calculate_day_timedelta(dow):
    td = dow - 3
    if dow < 3:
        return 4 + dow
    
    return td


def read_block_hours():
    with open(os.path.join(DATA_DIR,'market_block_hours.csv'), mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        block_hours = {}
        departure_week_cols = {}
        for i,row in enumerate(csv_reader):
            market = row[0]
            base = row[1]
            for j,col in enumerate(row):
                if j<1:
                    continue

                if i==0:
                    departure_week = dateutil.parser.parse(col)
                    block_hours[departure_week] = []
                    departure_week_cols[j] = departure_week
                else:
                    block_hours[departure_week_cols[j],market] = float(col)
    return block_hours

def read_capacity_plan():
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
    return capacity_plan

def combine_capacity_plan_and_block_hours(capacity_plan,block_hours):
    for dep_date in capacity_plan.keys():
        for i,r in enumerate(capacity_plan[dep_date]):
            dep_week = r[0]
            market = r[2]
            capacity_plan[dep_date][i].append(block_hours[dep_week,market])
    capacity_plan['header'] = ['departure_week','base','market','block_hours']
    return capacity_plan

def get_capacity_plan():
    capacity_plan = read_capacity_plan()
    block_hours   = read_block_hours()
    capacity_plan = combine_capacity_plan_and_block_hours(capacity_plan,block_hours)
    return capacity_plan



