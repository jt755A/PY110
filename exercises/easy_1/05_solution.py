def word_sizes(text):
    # words = text.split()
    # words_count = [len(word) for word in words]

    # return {len(word): words_count.count(len(word)) for word in words}

    # result = {}

    words_list = text.split()
    counts = {}

    for word in words_list:
        word_size = len(word)

        if word_size not in counts:
            counts[word_size] = 0
        
        counts[word_size] += 1

    return counts



# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})