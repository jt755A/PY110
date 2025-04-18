# input:
    - a number, and a "count" of digits to rotate

# output:
    - a rotated number

# Questions
    - only integers?

# Rules
#   - Explicit:
        - Move the "count" digit from the end TO the end of a number
        - Other digits shift to the left

# Implicit:
    - All digits are integers?


# Examples

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True

# Data Structures

- An integer for the input
- A list for the result


# Algorithm

1. Given "number", and "count" of digits to rotate
2. Convert "number" into a string called "string_number"
    - Then "string_number" into list called "digit_lst"
3. Remove digit "count" number of digits from the end of "number"
    - assign that to "last_digit"
4. Concatenate "last_digit" to end of "digit_lst"
5. Join all elements in "digit_lst"
6. Convert to integer
7. return integer