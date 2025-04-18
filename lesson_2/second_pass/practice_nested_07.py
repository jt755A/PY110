lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]


new_lst = []


# for inner_lst in lst:
#     sublist = []

#     for item in inner_lst:
#         if item % 3 == 0:
#             sublist.append(item)
    
#     new_lst.append(sublist)

# for inner_lst in lst:
#     sublist = [item for item in inner_lst if item % 3 == 0]
    
#     new_lst.append(sublist)

def divisible_by_3(sublist):
    return [num for num in sublist if num % 3 == 0]

new_lst = [divisible_by_3(sublist) for sublist in lst]
           



print(new_lst)
print(lst)
