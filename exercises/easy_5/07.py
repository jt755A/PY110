'''
Problem
create function that sums the digits of the integer provided as input

Rules:
    - Explicit:
        - input is a positive integer
        - only one argumenet
Examples
print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

Data Structures
- Strings to pull each "digit" from input
- integers: to loop through each digit and add to running total


Algorithm
1. Given "number" as input
2. Initialize variable "running_total" to 0
3. Iterate through "number", adding each "digit" to "running_total"
4. After iterating, return "running_total"

Alternative:
1. Given "number" as input
2. create list "digit_list" of made up of each "digit" in "number"
3. return the sum of each "element" in "digit_list"

'''

def sum_digits(number):
    # running_total = 0
    # for digit in str(number):
    #     running_total += int(digit)

    # return running_total

    digit_list = [int(digit) for digit in str(number)]
    return sum(digit_list)

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True
