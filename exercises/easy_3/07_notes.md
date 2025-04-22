# Input:
    A name as a string: First name, last name

# Output:
    - A new string: last name, ", ", first name

# Rules
#   - Explicit:
        - Returns new string
        - contains last name, comma, space, first name
        - Prefixes, suffixes are ignored


print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# Data Structure
    - Strings

# Algorithm
1. given "input"
2. Split "input" and assign strings to "first_name" and "last_name",
respectively.
3. return a new string that interpolates strings into required order.