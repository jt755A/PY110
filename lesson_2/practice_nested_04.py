munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

# names = list(munsters.keys())

# for name in names:
#     print(f'{name} is a {munsters[name]['age']}-year-old {munsters[name]['gender']}.')

for name, info in munsters.items():
    print(f'{name} is a {info['age']}-year-old {info['gender']}.')