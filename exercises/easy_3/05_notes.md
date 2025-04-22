# input:
    - Positive integer

# output:
    - INTEGER, with reversed digits


# Rules
#   - Explicit:
        - digits are reversed
        - integer is positive

# Implicit:
    - Leading zeroes in output are removed
    - 1 digit inputs are returned as-is

# Examples

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True

# Data Structures
    - Integers for input, output
    - strings for digit reversal

# Algorithm
1. given "input" integer
2. reverse digits
3. Remove any leading zeroes
4. return "output"

