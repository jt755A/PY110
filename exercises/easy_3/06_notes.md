# input:
    - positive integer

# output:
    - a LIST containing all integers from 1 to input, inclusive

# Rules
#    - Explicit:
        - Positive integer as argument
        - answer is list, made up of integers from 1 - argument
        - Ascending order

#   - Implicit:
        - If input is 1, answer contains 1, only.

# Test cases:

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True

# Data Structures:
    - Lists and ranges

# Algorithm:
1. given "input"
2. Initialize "result" to an empty list.
3. Starting from 1, add each integer up to "input" to "result"
4. return "result"