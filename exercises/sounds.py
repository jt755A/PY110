# Rules
    # Explicit:


# Algorithm
# 1. Create empty Dictionary 'sounds'




def sounds(dictionary):
    # Your Code Here
    sounds_lst = []
    for sound in dictionary.values():
        sounds_lst.append(sound + '-' + sound)

    # return sounds_lst

    return [(sound * 2) for sound in dictionary.values()]


animals = {'cow': 'moo', 'cat': 'meow', 'dog': 'woof'}
print(sounds(animals))  # ['moo-moo', 'meow-meow', 'woof-woof']


