import math

DEGREE = "\u00B0"
MINUTES_PER_DEGREE = 60
SECONDS_PER_MINUTE = 60
SECONDS_PER_DEGREE = MINUTES_PER_DEGREE * SECONDS_PER_MINUTE

UPPER_BOUND = 360
LOWER_BOUND = 0
INCREMENT = 360


def restrict_range(degree_float):
    check_float = degree_float
    
    while check_float > UPPER_BOUND:
        check_float -= INCREMENT
    
    while check_float < LOWER_BOUND:
        check_float += INCREMENT
    
    return check_float

        
# print(restrict_range(-1))
# print(restrict_range(400))
# print(restrict_range(-40))
# print(restrict_range(-420))
# print(restrict_range(69))
# print(restrict_range(0))
# print(restrict_range(360))


def pad_zeroes(number):
    num_string = str(number)
    if len(num_string) < 2:
        return '0' + num_string
    else:
        return num_string


def dms(angle):
    # degrees = math.floor(angle)
    # decimal_remainder = (angle % 1) * 100
    # minutes = math.floor(decimal_remainder * 0.6)
    # minutes_remainder = (decimal_remainder * 0.6) % 1
    # seconds = math.floor((minutes_remainder * 100) * 0.6)

    restricted_float = restrict_range(angle)

    # degrees_int = int(angle)
    degrees_int = int(restricted_float)

    # decimal_remainder = angle - degrees_int
    decimal_remainder = restricted_float - degrees_int

    minutes = int(decimal_remainder * MINUTES_PER_DEGREE)
    seconds = int(
        (decimal_remainder - (minutes / MINUTES_PER_DEGREE)) *
        SECONDS_PER_DEGREE
    )



    return (f"{degrees_int}{DEGREE}"
            f"{pad_zeroes(minutes)}'"
            f'{pad_zeroes(seconds)}"'
    )

# print(dms(30))
# print(dms(76.73))
# print(dms(254.6))
# print(dms(93.034773))
# print(dms(0))
# print(dms(360))





# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")



print(dms(-1))   # 359°00'00"
print(dms(400))  # 40°00'00"
print(dms(-40))  # 320°00'00"
print(dms(-420)) # 300°00'00"