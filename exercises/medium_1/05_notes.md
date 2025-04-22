# input:
    - a string

# output:
    - a string, with "number words" in original replaced with
    digit of that number

# Rules
#    - Explicit:
        - convert "number word" to 0, 1, 2, 3 etc
        - other string characters unaffected

#   - Implicit:
        - spaces are the delimiting character
        - 

# Examples

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

# Data Structures
    - dictionary: map digits to "number word"
    - lists: create sequential lists of words in message
    - strings

# Algorithm

1. Given "message" string
2. Initialize a "number_words" to empty dictionary
3. Add mappings of each word to its digit
4. Iterate over each "word" in message
    A. If a number word, convert to digit
    B. If not, leave as is
5. return converted "result"