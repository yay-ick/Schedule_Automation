import datetime


def schedule_stats(schedule):
    stats = {}

    max_lines = {}
    latest_finish = {}
    departures_by_period = {}
    for dep_date in schedule.keys():
        if dep_date=='cols':
            continue

        for base in schedule[dep_date].keys():
            if not base in max_lines:
                max_lines[base] = -1

            if not base in latest_finish:
                latest_finish[base] = datetime.datetime(1950,1,1)

            if not base in departures_by_period:
                departures_by_period[base] = {}
                departures_by_period[base]['early morning'] = 0
                departures_by_period[base]['late morning'] = 0
                departures_by_period[base]['early afternoon'] = 0
                departures_by_period[base]['late afternoon'] = 0
                departures_by_period[base]['evening'] = 0
            
            num_lines = len(schedule[dep_date][base])
            if num_lines > max_lines[base]:
                max_lines[base] = num_lines

            for line in schedule[dep_date][base]:
                for flight in line:
                    if flight['Arr Time']>latest_finish[base]:
                        latest_finish[base] = flight['Arr Time']
                
                    if flight['Dep Time'].time() >= datetime.datetime(2025,1,1,5,0).time() and flight['Dep Time'].time() < datetime.datetime(2025,1,1,8,30).time():
                        departures_by_period[base]['early morning'] += 1
                    elif flight['Dep Time'].time() >= datetime.datetime(2025,1,1,8,30).time() and flight['Dep Time'].time() < datetime.datetime(2025,1,1,12,0).time():
                        departures_by_period[base]['late morning'] += 1
                    elif flight['Dep Time'].time() >= datetime.datetime(2025,1,1,12,0).time() and flight['Dep Time'].time() < datetime.datetime(2025,1,1,15,30).time():
                        departures_by_period[base]['early afternoon'] += 1
                    elif flight['Dep Time'].time() >= datetime.datetime(2025,1,1,15,30).time() and flight['Dep Time'].time() < datetime.datetime(2025,1,1,19,0).time():
                        departures_by_period[base]['late afternoon'] += 1
                    elif flight['Dep Time'].time() >= datetime.datetime(2025,1,1,19,).time(): # and flight['Dep Time'].time() < datetime.datetime(2025,1,1,19,0).time():
                        departures_by_period[base]['evening'] += 1
                    
            
    stats['max_lines'] = max_lines
    stats['latest_finish'] = latest_finish
    stats['departures_by_period'] = departures_by_period

    return stats

