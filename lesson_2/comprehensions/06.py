lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# def increment_values(dictionary):
#     return {key: value + 1 for key, value in dictionary.items()}

# new_lst = [increment_values(value) for value in lst]

# print(new_lst, lst, sep='\n')


new_lst = [{key: value + 1 for key, value in dictionary.items()}
            for dictionary in lst]

print(new_lst)