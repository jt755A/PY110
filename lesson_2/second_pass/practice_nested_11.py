VOWELS = 'aeiou'

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = []

for value_list in dict1.values():
    for element in value_list:
        for char in element:
            if char in VOWELS:
                list_of_vowels.append(char)

list_of_vowels_2 = [char for value_list in dict1.values()
                    for word in value_list
                    for char in word if char in VOWELS]

# print(list_of_vowels)
print(list_of_vowels_2)

# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']


