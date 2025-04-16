# input: 2 lists

# output: function returns set

# rules:
#    - Explicit:
        - return value a set
        - contains element unique to first list

#   - Implicit:
        -

# Examples / test cases

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

# Algorithm

1. given "first_list", "second_list"
2. iterate through "first_list", selecting elements that are NOT in "list_2"
3. return results