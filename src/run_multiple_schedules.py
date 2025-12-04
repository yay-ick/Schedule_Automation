
# import numpy as np
# import pandas as pd
import datetime

import schedule_inputs
import schedule_builder
import schedule_analyzer
import schedule_outputs
import helper_tools



num_runs = 10
capacity_plan = schedule_inputs.get_capacity_plan()
station_constraints = schedule_inputs.read_station_constraints()

results = {}
for i in range(num_runs):
    print(i+1,'of',num_runs,end='')
    capacity_plan = helper_tools.randomize_capacity_plan(capacity_plan)

    start = datetime.datetime.now()
    schedule = schedule_builder.build_schedule(capacity_plan,station_constraints)
    end = datetime.datetime.now()
    dt = (end-start).seconds
    # ;;;; run schedule adjustments --- modify turn times and/or start times
    # ;;; run pairing optimization / head count forecast
    # ;;; run revenue forecast

    schedule_stats = schedule_analyzer.schedule_stats(schedule)
    print(', run time:',str(dt)+' seconds, lines:',schedule_stats['max_lines']['MSP'],'latest finish:',schedule_stats['latest_finish']['MSP'])

    results[i] = {}
    results[i]['capacity_plan'] = capacity_plan
    results[i]['schedule'] = schedule
    results[i]['stats'] = schedule_stats



