'''
Problem: convert a string of digits to an integer.
No using conversion functions


Examples:
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

Data Structures
Dicts: map integer value to a string digit

Algorithm

1. Given "int_string"
2. assign "result" to 0
3. Lookup value in dict

4. Multiply "digit" by powers of 10:
    - if last digit, 10**0
    - if 2nd to last, 10**1 etc
C

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

        print(result)
    
    return result
        
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True