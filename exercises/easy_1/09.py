'''
Problem
convert a "signed" number string into an integer, without using built in conversion
functions

    Input:
        - A number string, with or without a +/- sign

    Output:
        - integer with correct sign

    Rules:
        - Explicit:
            - if '-' precedes number: negative integer result
            - if '+' OR no sign: positive integer

Examples
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

Data Structures
    - ranges, string operations

Algorithm

1. given "string_num" input
2. Determine the "sign":
    A. If the first character is '-': negative
    B. if first character is '+' OR the key in "num_conversion" (a digit)
    --> then positive
3. Call "string_to_integer" function
4. Depending on "sign":
    - If positive: return the function call result as is (strip the ve sign)
    - If negative: negate the function call result (strip the -ve sign
Code
'''


def string_to_integer(int_string):
    result = 0
    multiplier = 1
    num_conversion = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0
    }
    for digit_idx in range(-1, -len(int_string) - 1, -1):
        
        value = num_conversion[int_string[digit_idx]] * multiplier
        result += value
        multiplier *= 10

        # print(result)
    
    return result

def string_to_signed_integer(num_string):
    match num_string[0]:
        case '-':
            return -(string_to_integer(num_string.strip('-')))
        
        case '+' | _:
            return string_to_integer(num_string.strip('+'))
        
print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True