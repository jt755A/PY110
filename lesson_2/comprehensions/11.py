VOWELS = 'aeiou'

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

list_of_vowels = []

for lst in dict1.values():
    for char in ''.join(lst):
        if char in VOWELS:
            list_of_vowels.append(char)

list_of_vowels = [char for lst in dict1.values()
                  for char in ''.join(lst)
                  if char in VOWELS]

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']