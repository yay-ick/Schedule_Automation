

import numpy as numpy
import pandas as pd

import inputs
import constraint_solver
import helper_tools





capacity_plan = inputs.get_capacity_plan()
station_constraints = inputs.read_station_constraints()

lines = {}
for dep_date in capacity_plan.keys():
    if dep_date=='header':
        continue

    if not dep_date in lines:
        lines[dep_date] = {}

    for flight_pair in capacity_plan[dep_date]:
        # dep_week = flight_pair[dep_date][capacity_plan['header']['departure_week']]
        base = flight_pair[capacity_plan['cols']['base']]
        market = flight_pair[capacity_plan['cols']['market']]
        # pattern = flight_pair[dep_date][capacity_plan['header']['pattern']]
        block_hours = flight_pair[capacity_plan['cols']['block_hours']]

        if not base in lines[dep_date]:
            lines[dep_date][base] = []

        orig,dest = helper_tools.get_ond(market,base)
        succes, earliest_departure_time = constraint_solver.find_earliest_departure_time(dep_date,orig,dest,base,block_hours,lines,station_constraints)
        # if success:
        #     lines = add_flight(;;;;)
        





