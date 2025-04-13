# input:
    - string
# output:
    - Boolean: True, or False

# rules
#   - Explicit:
        - checks if input is "palindrome"
            - palindrome is string that reads the same forwards and backwards
        - returns a Boolean
        - the case matters: 'A' is not equal to 'a'
        - all characters matter: whitespace, special characters included

#   - Implicit

# Test cases
# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

# Data structures
    - strings

# Algorithm
    1. given "input" string
    2. initalize a variable "reversed_input" to reverse of "input"
    3. Test for value equality between "input" and "reversed_input"
    4. Return result, as a Boolean

