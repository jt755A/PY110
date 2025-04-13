# input:
    - list
# output
    - function returning set

# rules
#   Explicit:
        - 2 arguments
        - both arguments will always be lists
        - return "union" of two values: unique values in each

#   Implicit:
        - lists could be empty
    
# Example
print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True

# Data Structure
    - input lists
    - set

# Algorithm

1. given lists "arg1" and "arg2"
2. set "combined_list" to concatenation of "arg1" and "arg2"
3. construct "result_set from "combined_list"
4. return "result_set"