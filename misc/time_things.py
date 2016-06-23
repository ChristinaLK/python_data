
def leap_year(yr):
    if yr % 4 != 0: 
        return 365
    elif yr % 1000 == 0:
        return 366
    elif yr % 100 == 0:
        return 365
        
def start_end(day):
    if 