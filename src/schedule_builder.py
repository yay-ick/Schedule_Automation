

import helper_tools
import constraint_solver
import datetime



def add_flight(orig,dest,dep_date,base,dep_datetime,block_hours,station_constraints,lines):

    flight = {}
    flight['Orig'] = orig
    flight['Dest'] = dest
    flight['Base'] = base
    flight['Dep_Date'] = dep_date.date()
    flight['Dep Time'] = dep_datetime
    flight['Arr Time'] = flight['Dep Time'] + datetime.timedelta(hours=block_hours)
    flight['Block Time'] = block_hours
    
    lines[dep_date][base][-1].append(flight)

    flight = {}
    flight['Orig'] = dest
    flight['Dest'] = orig
    flight['Base'] = base
    flight['Dep_Date'] = dep_date.date()
    flight['Dep Time'] = dep_datetime + datetime.timedelta(hours=block_hours) + datetime.timedelta(hours=station_constraints[dest]['Turn Time'])
    flight['Arr Time'] = flight['Dep Time'] + datetime.timedelta(hours=block_hours)
    flight['Block Time'] = block_hours
    
    lines[dep_date][base][-1].append(flight)

    return lines




def build_schedule(capacity_plan,station_constraints):
    lines = {}
    for dep_date in capacity_plan.keys():
        if dep_date=='cols':
            continue

        print(dep_date.date())

        if not dep_date in lines:
            lines[dep_date] = {}

        for flight_pair in capacity_plan[dep_date]:
            # dep_week = flight_pair[dep_date][capacity_plan['header']['departure_week']]
            base = flight_pair[capacity_plan['cols']['base']]
            market = flight_pair[capacity_plan['cols']['market']]
            # pattern = flight_pair[dep_date][capacity_plan['header']['pattern']]
            block_hours = flight_pair[capacity_plan['cols']['block_hours']]

            if not base in lines[dep_date]:
                lines[dep_date][base] = [[]]

            orig,dest = helper_tools.get_ond(market,base)
            success, dep_datetime = constraint_solver.find_earliest_departure_time(dep_date,orig,dest,base,block_hours,lines[dep_date][base],station_constraints)
            if success:
                lines = add_flight(orig,dest,dep_date,base,dep_datetime,block_hours,station_constraints,lines)

    return lines