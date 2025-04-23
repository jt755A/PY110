# Count the number of 'pair unique letters' in a given string.
# A pair unique letter is when two different letters appear in sequence.

# def count_unique_pairs(word):
#     # Implementation
#     unique_letter_pairs = 0
#     for idx in range(1, len(word)):
#         if word[idx] != word[idx - 1]:
#             unique_letter_pairs += 1

#     return unique_letter_pairs


def count_unique_pairs(word):
    # Implementation
    # unique_letter_pairs = {f'{word[idx-1]}{word[idx]}' for idx in range(1, len(word))
    #         if word[idx-1] != word[idx]}

    unique_letter_pairs = set()
    for idx in range(1, len(word)):
        if word[idx - 1] != word[idx]:
            unique_letter_pairs.add(f'{word[idx - 1]}{word[idx]}')
    
    return len(unique_letter_pairs)

# Tests
print(count_unique_pairs('abcddcba'))  # 6
print(count_unique_pairs('aabbcc'))    # 2
print(count_unique_pairs('abcdef'))    # 5


# Algorithm
# 1. make a range starting at index 1 ---> length of string
# 2. Initalize a "unique_letter_pairs" variable to 0
# 3. Iterating through each letter in range, if previous letter doesn't
# equal current letter:
#   - Increment letter
# 4. return "unique_letter_pairs"




# Count the number of 'pair unique letters' in a given string.
# A pair unique letter is when two different letters appear in sequence.


# Shannon's solution

"""
P
input: a word
output: an integer, represending the number of 'pair unique letters' - meaning, substring of 2 letters that are unique (not duplicate)
rules:
- input word is all lowercase

E
'abcddcba' => 'ab', 'bc', 'cd', 'dc', 'cb', 'ba'
'aabbcc' => 'ab', 'bc'
'abcdef' => 'ab', 'bc', 'cd', 'de', 'ef'


D
list

A
high-level: 
- get all substrings, remove ones containing duplicates, and any repeats (e.g. set())
- iterate through the word, looking at each pair of letters, and if the letters are unique, (and not already in my list) add the pair to a list of unique pairs

- initialize a list `unique_pairs` to []
- for i in range(1, len(word)): (starting at the second letter and going to the end of the word,)
    letter1, letter = word[i-1], word[i]

    if the letters are not the same, and if f'{letter1}{letter2}' is not in `unique pairs`, add this substring to unique_pairs

- return len(unique_pairs)

"""

# def count_unique_pairs(word):
#     unique_pairs = []
#     for i in range(1, len(word)):
#         letter1, letter2 = word[i-1], word[i]
#         substring = f'{word[i-1]}{word[i]}'
#         if letter1 != letter2 and (substring not in unique_pairs):
#             unique_pairs.append(substring)
#     return len(unique_pairs)

# # Tests
# print(count_unique_pairs('abcddcba'))  # 6
# print(count_unique_pairs('aabbcc'))    # 2
# print(count_unique_pairs('abcdef'))    # 5