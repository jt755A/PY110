# inputs:
    - list of strings

# output:
    - list of strings, with vowels removed

# questions
    - What if strings contain whitespace/special characters?
    - Should this work for non-ASCII characters?
    - What to return for an empty string?
    - What to return if a string only contains vowels?


# Rules
#   - Explicit:
        - return a list with "vowels" removed
        - "vowels" are (a, e, i, o, u)

#    - Implicit:
        - This function is case-insensitive: it should remove (a, A) etc
        - if a string is made up entirely of vowels, return an empty string
        - if no vowels in a string, return as is

# Examples

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True

# Data structures
    - strings
    - lists

# Algorithm
1. initialize a "VOWELS" constant containing all lower-case vowels
2. initialize "clean_lst" to an empty list
3. given "input_list" of strings to function
4. iterate through each "element" in "input_list"
    - assign "cleaned_element" to an empty string
    - iterate through each character in "element":
        - for each "char" in "element"
            - if lower case version of "char" is not in "VOWELS":
                - concatenate 'char' to "cleaned_element"
    - add "cleaned_element" to end of "clean_lst"

6. return "clean_lst"
