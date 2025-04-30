'''

Problem
Write a function taking string as argument. Returns a list that contains
each word in string, plus its length (after a space)
e.g. 'hello 5'....

# Input:
    - string as argument

# Output:
    A list with strings plus their length

# Rules
    Explicit:
    - output: the word itself, then space, then its length (as an integer)
    - If argument is empty string/no argument supplied: empty list

    Implicit:
        - a "word" is a string separated by a single ' ' whitespace.
        - Punctuation/Special characters are included: ",", "'", "?" etc

Examples/test cases
# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True

Data structures
- Form a list of "words" in input

Algorithm

1. Given "input_string"
    - set an empty string as default parameter, in case no argument supplied
2. Split each "word" from "input_string"
3. Add each word, plus its length, to "output_lst"
4. return "output_lst"

'''

def word_lengths(input_str=''):
    # split_words = input_str.split()
    # output_lst = []

    # for word in split_words:
    #     output_lst.append(f'{word} {len(word)}')

    # return output_lst

    return [f'{word} {len(word)}' for word in input_str.split()]

words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True