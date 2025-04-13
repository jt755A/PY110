# input:
    - string: 24 hour time in hh:mm format

# output:
    - returns an integer (both functions)

# Rules
#    - Explicit:
        - positive integers are after midnight
        - negative integers are before midnight
        - answers should be in range 0 - 1439 (number
        of minutes in a day)

#   - Implicit:
        -

# Examples

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

# Structures
integers

# Algorithm

1. set constants: MINUTES_PER_HOUR, HOURS_PER_DAY, MINUTES_PER_DAY

2. given "time"
3. extract "hours" component (first 2 numbers)
4. extract "minutes" component (last 2 numbers)
5. calculate "total_minutes":
    - ("hours" * MINUTES_PER_HOUR) + "minutes"
6. return "total_minutes"


    # After midnight
    1. "cleaned_time" = result of "total_time" function call on input
    2. return "cleaned_time" modulo "MINUTES_PER_DAY"


    # Before midnight
    1. return reaminder of ("MINUTES_PER_DAY" - "total_minutes") and
    MINUTES_PER_DAY

