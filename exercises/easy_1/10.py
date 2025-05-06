'''
Problem
Convert a non-negative integer into a string, without using built-in
conversion functions

Input:
    - a non-negative integer

Ouput: 
    - a string representation of that number

Examples

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

Data Structures
Integer functions

Algorithm
1. Given "number"
2. Extract each digit from "number", into 1 element list
    - first digit = modulo 10
    - second digit 
3. Reverse list in place
3. Combine and return these digits as a string representation.

1. Maximum power of 10 is when power of 10 % "input" equals "input"


C


'''
NUM_CONVERSION = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        0: '0'
    }

def integer_to_string(number):
    result = []
    while True:

        digit = number % 10
        result.append(NUM_CONVERSION[digit])
        number = number // 10
        # print(result)
        if number == 0:
            break

    result.reverse()
       
    return ''.join(result)







# def max_power_10(number):
#     power_of_10_idx = 0
#     while number != number % 10**power_of_10_idx:
#         power_of_10_idx += 1

#     return power_of_10_idx


# def integer_to_string(number):
#     for idx in range(1, max_power_10(number) + 1):
#         current_value = number % 10**idx
#         print(current_value)



# def integer_to_string(number):
#     power_of_10_idx = 1
#     value_lst = []
#     while power_of_10_idx < 10:
#         current_value = number % 10**power_of_10_idx
#         value_lst.append(current_value)
#         power_of_10_idx += 1

#     return value_lst

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

# print(max_power_10(4321))
# print(max_power_10(0))
