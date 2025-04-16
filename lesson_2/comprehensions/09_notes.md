# input: a list of dictionaries
    - dictionaries contain nested dictionaries: values are lists

# output:
    - FUNCTION that returns a list with nested dictionary, where all values are even

# rules

#   - Explicit:
        - all values in list of dictionary must be even 

#   - Implicit:
        - returning a whole 'outer' dictionary

# questions:
    - sub-dictionaries or whole dicts returned?
        - Answeer from example: ALL subdicts must have even values to qualify

# Examples

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# Data structures
    - dicts
    - list comprehensions

# Algorithm

1. given "input_lst" of dictionaries
2. iterate through "dictionary" in input_lst
3. determine if all "list_values" in "dictionary" are even
    - iterate through all "nums" in "dictionary"
        - determine if all "nums" in "dictionary" are even
        - 

# helper function
#   - is_even(list)

1. given "num" in "list"
2. iterate through "nums" in "list
3. create list with results of whether "num" is even
4. if all elements in step 3 are even:
    - return True
    - Else, return False

# helper function
#    - all_even(dictionary)

1. given "list_values" in "dictionary"
2. iterate through "list_values"
3. call is_even(list) on each "list_value"
4. create a list with all results of step 3.
5. if all elements in step 4 are even:
    - return True
    - Else, return False
