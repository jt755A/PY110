CONSONANTS = 'bcdfghjklmnpqrstvwzyz'
VOWELS = 'aeiou'

def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    
    return strings     
   
def count_max_adjacent_consonants(string):
    string = string.replace(' ','')
    maximum_consonants_count = 0
    adjacent_consonants_string = ''
    for letter in string:
        if letter.casefold() in CONSONANTS:
            adjacent_consonants_string += letter
            if len(adjacent_consonants_string) > maximum_consonants_count:
                    maximum_consonants_count = len(adjacent_consonants_string)
            
        
        if letter.casefold() in VOWELS:
            if len(adjacent_consonants_string) > 1:    
                if len(adjacent_consonants_string) > maximum_consonants_count:
                    maximum_consonants_count = len(adjacent_consonants_string)

            adjacent_consonants_string = ''

       
    return maximum_consonants_count


# print(count_max_adjacent_consonants('dddaa'))       # 3
# print(count_max_adjacent_consonants('ccaa'))        # 2
# print(count_max_adjacent_consonants('baa'))         # 0
# print(count_max_adjacent_consonants('aa'))          # 0
# print(count_max_adjacent_consonants('rstafgdjecc')) # 4


# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# # # ['dddaa', 'ccaa', 'aa', 'baa']

# my_list = ['can can', 'toucan', 'batman', 'salt pan']
# print(sort_by_consonant_count(my_list))
# # ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
