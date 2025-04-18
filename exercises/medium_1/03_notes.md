# input:
    - integer

# output:
    - max rotated integer

# rules
    - rotate 1st character to end
    - then 2nd to end
    - then .... until final character

# implicit:
    - An input with 1 digit is returned as is


# Examples

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True

# Data Structures

lists

# Algorithm

1. Given "input" number
2. Determine "length" of digits in "input" 
3. Rotate the first digit to the end
4. Rotate the second digit of step 3 to the end
5. ... continue until you've rotated all characters
6. return result


# Problem: rotating first character to end

