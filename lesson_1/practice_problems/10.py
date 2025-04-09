dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem())

# prints 'bear'
# last item in collection is selected, value returned, key-value pair is deleted

# edit: incorrect: returns last key-value pair as a tuple ('b', 'bear').
# from Python 3.7 onwards