munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# male_age = 0
# male_ages = []

# for name_key in munsters:
#     if munsters[name_key]['gender'] == 'male':
#         male_ages.append(munsters[name_key]['age'])

# total_ages = sum(male_ages)
# print(total_ages)



total_male_ages = sum([munsters[name]['age'] for name in munsters
             if munsters[name]['gender'] == 'male'])


print(total_male_ages)
