# input:
    - string

# output:
    - string with double characters of input

# rules:
#    - Explicit:
        - every character in input is doubled in order
        
#   - Implicit:
        - Whitespace is included
        - empty strings returned as empty string

# Examples

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

# Data Structures

strings

# Algorithm

1. given "str"
2. assign "result" to empty string
3. iterate through every character in "str":
    append "str" twice to "result"
4. return "result"