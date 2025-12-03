


def get_ond(market,base):
    orig = market[:3]
    dest = market[-3:]
    if orig!=base:
        orig = market[-3:]
        dest = market[:3]
    
    return orig,dest