

import helper_tools
import datetime


def is_compliant(orig,dest,epdt1,epat1,epdt2,epat2,current_line_index,lines,constraints):

    #check easiest and fastest constraints first

    #check airport 1
    if   (epdt1 < constraints[orig]['Earliest Departure']
       or epat2 < constraints[orig]['Earliest Arrival']
       or epdt1 > constraints[orig]['Latest Departure']
       or epat2 > constraints[orig]['Latest Arrival']):
       return False

    #check airport 2
    if   (epdt2 < constraints[dest]['Earliest Departure']
       or epat1 < constraints[dest]['Earliest Arrival']
       or epdt2 > constraints[dest]['Latest Departure']
       or epat1 > constraints[dest]['Latest Arrival']):
       return False
       
    #turn times should be progmatically set and no violations should be allowed

    for line in lines:
        for flight in line:
            #departure separate at leg 1 origin
            if flight['Origin']==orig:
                dt = abs((epdt1 - flight['Dep Time']).hours)
                if dt < constraints[orig]['Departure Separation']:
                    return False

            #arrival separate at leg 1 destnionat
            if flight['Destination']==dest:
                dt = abs((epat1 - flight['Arr Time']).hours)
                if dt < constraints[dest]['Arrival Separation']:
                    return False

            #departure separate at leg 2 origin
            if flight['Origin']==dest:
                dt = abs((epdt2 - flight['Dep Time']).hours)
                if dt < constraints[dest]['Departure Separation']:
                    return False

            #arrival separate at leg 2 destnionat
            if flight['Destination']==orig:
                dt = abs((epat2 - flight['Arr Time']).hours)
                if dt < constraints[orig]['Arrival Separation']:
                    return False
    
    return True


    




def find_earliest_departure_time(dep_date,orig,dest,base,block_hours,lines,constraints):

    search_cut_off = datetime.timedelta(days=1) + datetime.datetime(dep_date.year,dep_date.month,dep_date.day,constraints[orig]['Earliest Arrival'].hour,constraints[orig]['Earliest Arrival'].minute,0)
    dt = 1.0 / 60 #1 minute increment
    t = -dt
    for i,line in enumerate)lines):

        turn1 = datetime.timedelta(hours=constraints[orig]['Turn Time'])
        turn2 = datetime.timedelta(hours=constraints[dest]['Turn Time'])

        block = datetime.timedelta(hours=block_hours)


        #earliest possible departure time
        t += dt
        epdt1 = line[-1]['Arr Time'] + turn1 + t
        epat1 = epdt1 + block

        epdt2 = epat1 + turn2
        epat2 = epdt2 + block

        # step minute by minute
        while epat2 < search_cut_off:
            if is_compliant(i,lines,epdt1,epat1,epdt2,epat2,constraints):
                return True, epdt1
        
        return False, None
        
        










