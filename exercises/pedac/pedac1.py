'''
=begin
/*
Detect Pangram
A pangram is a sentence that contains every single letter of the alphabet at least once.  
For example: the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. 
Return True if it is, False if not. Ignore numbers and punctuation.
*/

// Javascript test cases:
console.log(isPangram('The quick brown fox jumps over the lazy dog.') == true)
console.log(isPangram('This is not a pangram.') == false)

// # Python test cases:
// print(isPangram('The quick brown fox jumps over the lazy dog.') == True)
// print(isPangram('This is not a pangram.') == False)

// # Ruby test cases:
p (isPangram('The quick brown fox jumps over the lazy dog.') == true)
p (isPangram('This is not a pangram.') == false)
=end

'''

'''
# Problem
    - Input:
        - a string
    - Output:
        - return a Boolean if it is or not a 'Pangram'

# Rules
    - Explicit 
        - a pangram is a string that contains all letters of alphabet AT LEAST ONCE
        - case is irrelvant

# Implicit
    - Ignore punctuation.

EExamples
print(isPangram('The quick brown fox jumps over the lazy dog.') == True)
// print(isPangram('This is not a pangram.') == False)


# Data structure
    - A string for sentence
    - A constant string for "Alphabet"


# Algorithm

1. given "sentence" input string
2. Initialize a constant 'ALPHABET' to all characters in alphabet
3. Initialize a "letter_in_sentence" to an empty list
4. Iterate through each "character" in 'ALPHABET', check if each "character" is in "sentence" (lower-cased)
    - Add the Boolean result to "letter_in_sentence"
5.  Return the result of checking if ALL elements are truthy

alphabet = 'abcdefghijklmnopqrstuvwzyz'
or 
or alphabet, and ascii

'''
ALPHABET = 'abcdefghijklmnopqrstuvwzyz'

def isPangram(sentence):
    # letter_in_sentence = [char in sentence.casefold() for char in ALPHABET]
    # return all(letter_in_sentence)

    letter_in_sentence = []
    for char in ALPHABET:
        letter_in_sentence.append(char in sentence.casefold())
        print(f'{char} in sentence: {char in sentence.casefold()}')
    
    return all(letter_in_sentence)

    # letter_in_sentence = [char in sentence.casefold() for char in ALPHABET]
    # return all(letter_in_sentence)

print(isPangram('The quick brown fox jumps over the lazy dog.') == True)
print(isPangram('This is not a pangram.') == False)

        
    

    