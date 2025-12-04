
import random

def get_ond(market,base):
    orig = market[:3]
    dest = market[-3:]
    if orig!=base:
        orig = market[-3:]
        dest = market[:3]
    
    return orig,dest



def randomize_capacity_plan(capacity_plan):
    for dep_date in capacity_plan.keys():
        if dep_date=='cols':
            continue
        x = capacity_plan[dep_date]
        random.shuffle(capacity_plan[dep_date])
    
    return capacity_plan


