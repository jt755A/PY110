VOWELS = ['a', 'e', 'i', 'o', 'u']

def remove_vowels(string_list):
    clean_lst = []

    for element in string_list:     
        cleaned_element = ''

        for char in element:            
            if char.casefold() not in VOWELS:
                cleaned_element += char

        clean_lst.append(cleaned_element)

    return clean_lst

original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True