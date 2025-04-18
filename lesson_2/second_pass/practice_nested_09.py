lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

result = []

for dictionary in lst:

    is_even_dictionary = []

    for value_list in dictionary.values():
        
        is_even_element = []
        
        for element in value_list:
            is_even_element.append(element % 2 == 0)

        is_even_value_list = all(is_even_element)
        is_even_dictionary.append(is_even_value_list)

    all_even_dictionary = all(is_even_dictionary)

    if all_even_dictionary:
        result.append(dictionary)

    

# def is_even_list(sublist):
#     return all([element % 2 == 0 for element in sublist])

# def all_even(dictionary):
#     all_sublists = [is_even_list(value_list) for value_list in dictionary.values()]
#     return all(all_sublists)


# result = [dictionary for dictionary in lst
#           if all_even(dictionary)]

print(result)

# print(all_even({'a': [1, 2, 3]}))
# print(all_even({'b': [2, 4, 6], 'c': [3, 6], 'd': [4]}))
# print(all_even({'e': [8], 'f': [6, 10]}))


# result = [dictionary for dictionary in lst
#           if 
    