lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

# new_dict = dict(lst)
# print(new_dict)

new_dict = {sublist[0]:sublist[1] for sublist in lst}
print(new_dict)