## Problem

- Input: list of strings
- Output: a new sorted list of strings

# Rules

#   - Explicit
        - sort string order in new list by highest adjacent consonants
        - consonants are adjacent if they are:
            - next to each other in a word
            - separated by a space in adjacent words
        - If two strings contain same number of consonants, sort them by
        their original order in input list.
        - Strings are added to list as-is.
#   - Implicit
        - Strings in list can have multiple words
        - Strings may not be empty
        - Sorted in descending order
        - Strings can contain no consonants
        - Case is not relevant
#       - Single consonants in string do not affect sort order comopared to 
#       strings with no consonants

# Questions
    - Do strings always have multiple words?
        - no
    - Can there be empty strings?
        - none included
    - Is this test case-sensitive?
        - all strings provided are lower-case. Can ignore?
    - What to return if a string contains no consonants?
        - return the string as-is
    - Are they sorted in ascending or descending order?
        - Descending order
    - What is a "space between" consonants? - Multiple whitespace, or just single?
        - Single space is only example given in examples

## Examples/Test cases

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']


## Data Structures

- An input list of strings
- a function to determine number of adjacent consonants
- sorting based on number returned by function, per string


# Algorithm

1. Given "input" list of strings
2. Iterate through each "string" in input
3. return a number of adjacent consonants in "string"
    - helper function
4. sort based on result from step 3

# Helper Function

# input:
    - string

# Output
    - integer

# rules:
    - counts number of adjacent consonants in string
    - whitespace can be removed between words in string

# Data structure
    - Strings

# Algorithm
1. define "consonants" string 'bcdfghjklmnpqrstvwxyz'
2. Given "string"
    - remove spaces
3. Initialize "adjacent_consonants" to 0
4. Iterate through "chars" in "string"
    A. return "adjacent_consonants" if length of string is less than or equal to 1
    B. Initialize "current_char" to 1
    B. if character is not a consonant
        - go to next character
    C. If character is a consonant
        - Check if previous character is a consonant
            - If so, increment "adjacent_consonants" by 1.

5. return value of "adjacent_consonants"

