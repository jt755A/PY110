# def keep_keys(my_dict, keys_lst):
#     return {key:value for key, value in my_dict.items()
#             if key in keys_lst}

def keep_keys(my_dict, my_keys):
    new_dict = {}
    for key in my_dict:
        if key in my_keys:
            new_dict[key] = my_dict[key]

    return new_dict

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True