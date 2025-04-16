# inputs:
    - dictionary, keys list

# output:
    - function returns a new dictionary

# rules:
#   Explicit:
        - only key/value pairs that contain listed keys are in dictionary

# Examples

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

# Data structure
    - dicts

# Algorithm
1. given "my_dict", "my_keys"
1. iterate through keys of "my_dict":
    - if "key" is in "my_keys":
        - add element to 'new_dict' as "key":"value"
3. return "new_dict"