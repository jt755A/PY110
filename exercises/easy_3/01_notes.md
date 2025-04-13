# input
    - integer representing minutes before or after midnight

# output
    - string of time represented in 24 hour format: hh:mm

# rules
#   Explicit:
        - input can be positive, negative, and zero integers
        - can't use datetime module
        - clock changes not considered: all times in past days are
        separated by multiples of 24 hours
    
#   Implicit:
        - must work for greater than one day ahead/behind current day

# Examples    
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

# Data structures
integers

# Algorithm

1. given integer "time"
2. set constant "MINUTES_PER_HOUR" to 60
3. initialize "result" to 0
4. set "hours" to floor quotient of "time" divided by "MINUTES_PER_HOUR"
    
5. set "minutes" to remainder of time and "hours" * "MINUTES_PER_HOUR"

6. - while "hours" >= 24:
        "hours" = "hours" - 24

6. return "result" interpolating "hours" and "minutes"
    - call "zeroes_padding" function on "hours" and "minute" to show 2 digits
    for each value


1. given integer "time"
2. calculate how many minutes "time" contains, relative to a single day
    - while absolute value of "time" >= "MINUTES_PER_DAY":
        - "time" minus "MINUTES_PER_DAY"
3. if "time" is positive ....
4. if "time" is negative ....







# follow up 

# adding days per week

# structures
    # dicts: delta integers mapped to Days of week

# Algorithm

1. create "DAYS_OF_WEEK" dict, relative to Sunday midnight
    - 0: Sunday, 1: Monday etc

2. Initialize "DAYS_PER_WEEK" constant

2. initialize "delta_days"
    - "total_minutes" floor quotient  MINUTES_PER_DAY 

3. resolve "delta_days" into 0 to 6
        -while "delta_days" < 0:
            "delta_days" = "delta_days" + "DAYS_PER_WEEK"

        "delta_days" = remainder of 7

