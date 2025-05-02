'''
Problem
Write a function that swaps FIRST AND LAST letter in each word of
input string.

Input:
    - A string

Output:
    - A new 'swapped' string

Rules:
    - Explicit:
        - a "word" is separated by single space (no leading, trailing,
        repeated spaces)
        - Each input string will contain at least one word
    
    - Implicit: 
        - case-sensitive
        - If a word contains one letter, it's unchanged?

Examples

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

Data Structures

String operations
    - Keeping track of first and last letter by indexing?

Algorithm

1. Given "string", split the string into a list of words.
Name this "word_lst"

2. For each "word" in "word_lst":
     Swap first and last letters
    - if "word" has only 1 letter, leave it
    - else: assign "first_letter" to first in word, "last_letter" to
    last in word
        - concatenate with rest of word.

3. Combine all "words" in "word_lst" to a string, separated by single
space (' ')

C
'''

def swap(string):
    word_lst = string.split()
    # print(word_lst)
    for idx in range(len(word_lst)):
        if len(word_lst[idx]) == 1:
            continue
        first = word_lst[idx][0]
        last = word_lst[idx][-1]
        middle = word_lst[idx][1:-1]
        word_lst[idx] = last + middle + first       
         
    return ' '.join(word_lst)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True