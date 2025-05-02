'''
Problem
Write a function that finds the next "featured number" above the integer
provdied as argument. A featured number is an odd, multiple of 7, with
no repeating digits.

Inputs:
    - An integer

Output:
    - Returns the next featured number - as an integer

Rules:
    - Explicit:
        - featured number is an odd, multiple of 7, with
        no repeating digits.
        - return the next featured number GREATER than argument
        - Largest possible featured number is 9876543201
        - Provide an error message if there is no greater featured number

Examples

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True

Data Structures
Integers
Converting to string - to check for repeating digits
if, elif ... block to check if featured number

Algorithm

1. Given "integer_input" as input
2. Start checking each integer above "integer_input" until
a number is a featured number.
    A. Initialize "result" to "integer_input" + 1
    B. check if "result" if featured number
        - if that's impossible, return error message
        - If not: increment "result" by 1
        - If it is: go to step 3
3. Return that number.

Helper function for step 2.B.

Algorithm

1. check if "result" is odd:
    - If even: "result" is not a featured number.
        - continue
    - If odd: go to next step

2. Check if "result" is multiple of 7:
    - If not: continue
    - If yes: go to next step

3. Check if any "digit" in "result" repeats
    - iterate through each "digit", checking if any
    has a count of greater than 1 (or all have count of 1)
        - If so, this is a featured number

C
'''
MAX_FEATURED_NUM = 9876543201

def next_featured(integer_input):
    if integer_input >= MAX_FEATURED_NUM:
        return ("There is no possible number that "
        "fulfills those requirements.")
    
    result = integer_input


    while True:
        result += 1
        if result % 2 == 0:
            continue
        
        elif result % 7 != 0:
            continue

        else:
            digit_count = [str(result).count(digit) == 1 for digit in str(result)]
            if all(digit_count):
                return result
            continue
        

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True