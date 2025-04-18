def adjacent_consonant_count(string):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    clean_string = ''.join(string.split())
    adjacent_consonants_string = ''
    max_adjacent_consonants = 0

    for char in clean_string:
        if char in consonants:
            adjacent_consonants_string += char
            
            if len(adjacent_consonants_string) > max_adjacent_consonants:
                if len(adjacent_consonants_string) > 1:
                    max_adjacent_consonants = len(adjacent_consonants_string)

        else:
            if len(adjacent_consonants_string) > max_adjacent_consonants:
                if len(adjacent_consonants_string) > 1:
                    max_adjacent_consonants = len(adjacent_consonants_string)

            adjacent_consonants_string = ''

    return max_adjacent_consonants


def sort_by_consonant_count(lst):
     return sorted(lst, key=adjacent_consonant_count, reverse=True)


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']