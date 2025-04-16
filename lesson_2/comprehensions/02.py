lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# new_lst = []

# for sublist in lst:
#     new_lst.append(sorted(sublist))

# print(new_lst)

new_lst = [sorted(sublist) for sublist in lst]
print(new_lst)