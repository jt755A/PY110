lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def list_is_even(my_lst):
    return all([num % 2 == 0 for num in my_lst])

def all_even(dictionary):
    lists_are_even = [list_is_even(list_value)
                      for list_value in dictionary.values()]
    return all(lists_are_even)

result = [dictionary for dictionary in lst
          if all_even(dictionary)]
print(result)