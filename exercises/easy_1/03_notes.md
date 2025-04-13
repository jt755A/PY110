# input:
    - string
# output:
    - Boolean: True, or False

# rules
#   - Explicit:
        - checks if input is real "palindrome"
            - palindrome is string that reads the same forwards and backwards
        - returns a Boolean
        - the case insenstive: 'A' is equal to 'a'
        - Only alpha-numeric characters matter: whitespace, special characters are excluded

#   - Implicit

# Test cases
print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

# Data structures
    - strings

# Algorithm
    1. given "input" string
    2. initialize "test" variable to empty string
    3. for each character in "input":
        - if character is alpha-numeric:
            - append casefolded character to "test"
        
    4. initalize a variable "reversed_input" to reverse of "input"
    5. return result of value equality test between "input" and "reversed_input"

