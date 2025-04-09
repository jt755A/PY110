input: list of strings
output: return a list

rules:
    explicit:
        - consonants are adjacent in a STRING if next to each in a word
        - adjacent if a space separates consonants in adjacent words of a string
        - if multiple strings contain same number of consonants, sort by relative position in original string

    implicit:
        - EDIT: strings can contain more than one word
        - case not relevant
        - strings may not be empty
        - strings can have no adjacent consonants
        - strings should be sorted in descending order
        - single consonants in string do not affect sort order

questions:
    - what is a word? Just whitespace separation?
    - does case matter?
        - assuming no
    - can strings be empty?
        -(assuming no)
    - should strings be sorted in descending or ascending order?
        - descending
    - can strings have no adjacent consonants
        -yes, e.g. example 1.


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


Data structures:
    - lists for data
    - dict to map # of adjacent consonants per string, and original position in string


Alogrithm:
    1. Determine how many adjacent consonants are in each string of input
    2. sort in descending order of adjacent consonants
        - check if list contains other strings with equal number of adjacent consonants
        - sort by relative position
    3. return sorted list



1. given input list:
    - determine how many adjacent consonants in each string
        - (write sub-process)
    - make a dictionary mapping 





max adjacent consonant function

- given "input string"
    - remove spaces from "input string"
    - initialize "maximum_consonant_string" to zero.
    - initialize "adjacent consonants string" to empty string
    - For each "letter" in "input string":
        - If "letter" is consonant:
            - concatenate to "adjacent consonants string"
            - If "adjacent consonants string" has length greater
                than 1:
                    - set "maximum consonants count" to length of
                    "adjacent consonants string".
        - else if "letter" is a vowel:
            - If "adjacent consonants string" has length greater
            greater than current "maximum consonants count":
                - If "adjacent consonants string" has length greater
                than 1:
                    - set "maximum consonants count" to length of
                    "adjacent consonants string".
        - reset "adjacent consonants string" to empty string

- Return maximum consonants string