

# import numpy as np
# import pandas as pd
import datetime

import schedule_inputs
import schedule_builder
import schedule_analyzer
import schedule_outputs






if __name__ == '__main__':
    capacity_plan = schedule_inputs.get_capacity_plan()
    station_constraints = schedule_inputs.read_station_constraints()
    schedule = schedule_builder.build_schedule(capacity_plan,station_constraints)
    schedule_outputs.output_csv(schedule)







