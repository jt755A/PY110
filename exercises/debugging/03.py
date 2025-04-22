# def get_key_value(my_dict, key):
#     if my_dict[key]:
#         return my_dict[key]
#     else:
#         return None
    
def get_key_value(my_dict, key):
    return my_dict.get(key, None)

print(get_key_value({"a": 1}, "b"))

# original code throws KeyError, because "b" is not a key in dict.
# Line 2 tries to access the non-existent value associated with key 'b'.
# Since this key is not in the dictionary, there will be an error.