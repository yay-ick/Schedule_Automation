
import os
import csv

OUTPUT_DIR = os.path.join('..','outputs')

def output_csv(schedule):

    # cols = {}
    # cols['base']           = 0
    # cols['departure date'] = 1
    # cols['line number']    = 2
    # cols['origin']         = 3
    # cols['destination']    = 4
    # cols['departure time'] = 5
    # cols['arrival time']   = 6

    output = [['base','departure date','line number','origin','destination','departure','arrival','block']]
    for dep_date in schedule.keys():
        for base in schedule[dep_date].keys():
            for i_line,line in enumerate(schedule[dep_date][base]):
                for flight in line:
                    row = [flight['Base']
                          ,flight['Dep Date']
                          ,i_line
                          ,flight['Orig']
                          ,flight['Dest']
                          ,flight['Dep Time']
                          ,flight['Arr Time']
                          ,flight['Block Time']
                          ]
                    output.append(row)

    output_filename = "schedule_output.csv"
    with open(os.path.join(OUTPUT_DIR,output_filename), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(output)
