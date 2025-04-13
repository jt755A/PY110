MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def total_minutes(hh_mm):
    # nonlocal hours; minutes; total_minutes
    
    split_time = hh_mm.split(':')                             
    
    hours = int(split_time[0])
    minutes = int(split_time[-1])

    total_minutes = (hours * MINUTES_PER_HOUR) + minutes

    return total_minutes

def after_midnight(time):
    return total_minutes(time) % MINUTES_PER_DAY

def before_midnight(time):
    return (MINUTES_PER_DAY - total_minutes(time)) % MINUTES_PER_DAY    
    

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True