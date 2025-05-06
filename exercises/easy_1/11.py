'''
Expand the last function to include sign

Algorithm:
1. Given "number"
2. Prepend the appropriate sign to the return result of last function:
    - if "number" positive: prepend a '+'
    - if "number" negative: prepend  '-'
    - else, just return the number

correct input for negative numbers to avoid infinite loop in 
"integer_to_string" function
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
    # number = abs(number)
    while True:

        digit = number % 10
        result.append(NUM_CONVERSION[digit])
        number = number // 10
        # print(result)
        if number == 0:
            break

    result.reverse()
       
    return ''.join(result)

# def signed_integer_to_string(number):
#     string_num = integer_to_string(number)
    
#     if number > 0:
#         return '+' + string_num
#     elif number < 0:
#         return '-' + string_num
#     else:
#         return string_num
    
def signed_integer_to_string(number):
    if number < 0:
        return f"-{integer_to_string(-number)}"
    elif number > 0:
        return f"+{integer_to_string(number)}"
    else:
        return "0"
    
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True