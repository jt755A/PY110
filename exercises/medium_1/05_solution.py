NUM_WORDS = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }



def word_to_digit(sentence):
    
    # result = []

    # for word in sentence.split():
    #     if word.casefold() in NUM_WORDS:
    #         result.append(NUM_WORDS[word])
        
    #     else:
    #         result.append(word)
        
    # return ' '.join(result)

    words = sentence.split()
    processed_words = [NUM_WORDS.get(word, word) for word in words]
    return ' '.join(processed_words)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")