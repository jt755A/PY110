# INPUT: list of integers

# output:
    - a function that returns list of integers, sorted by ENGLISH word alphabetically

# Rules
    - Implicit: use lowercase english words
    - ascending alphabetical sort: a - z

# example

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True

# Data Structures

- lists
- dicts

# Algorithm

1. Given "input_list"
2. create "num_word_list" with English words of each number in order
3. create "alpha_num_dict" mapping each number in "input_list" to
corresponding "num_word_list"
    - iterate through "input_list":
        - at each index, map each "word" to "number"
4. sort ascending order
5. return new list