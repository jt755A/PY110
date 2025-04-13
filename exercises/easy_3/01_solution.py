

MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = MINUTES_PER_HOUR * HOURS_PER_DAY
DAYS_PER_WEEK = 7

DAYS_OF_WEEK = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}


def zeroes_padding(num):
    str_num = str(num)
    if len(str_num) < 2:
        return "0" + str_num
    else:
        return str_num

def time_of_day(time):
    
    new_time = cleaned_time(time)

    delta_days = time // MINUTES_PER_DAY

    while delta_days < 0:
        delta_days += DAYS_PER_WEEK

    delta_days = delta_days % DAYS_PER_WEEK


    hours = new_time // MINUTES_PER_HOUR

    minutes = new_time - (hours * MINUTES_PER_HOUR)

    return (
        f'{DAYS_OF_WEEK[delta_days]} '
        # f'{zeroes_padding(hours)}:'
        f'{hours:02d}:'
        # f'{zeroes_padding(minutes)}'
        f'{minutes:02d}'

        )

    

def cleaned_time(num):
    if num >= 0:
        time_clean = num
        while time_clean >= MINUTES_PER_DAY:
            time_clean -= MINUTES_PER_DAY

    else:
        time_clean = num
        while time_clean < 0:
            time_clean += MINUTES_PER_DAY
    
    return time_clean

    
    
    
    # result = 0
    # hours = time // MINUTES_PER_HOUR

    # minutes = time - (hours * MINUTES_PER_HOUR)
    
    # while hours >= 24:
    #     hours -= 24



    return (f'{zeroes_padding(hours)}:'
            f'{zeroes_padding(minutes)}')













print(time_of_day(0)) #== "00:00")        # True
print(time_of_day(-3)) #== "23:57")       # True
print(time_of_day(35)) #== "00:35")       # True
print(time_of_day(-1437)) #== "00:03")    # True
print(time_of_day(3000)) #== "02:00")     # True
print(time_of_day(800)) #== "13:20")      # True
print(time_of_day(-4231)) #== "01:29")    # True