lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# new_lst = []

# for inner_lst in lst:
#     multiples_of_3 = []
    
#     for num in inner_lst:
#         if num % 3 == 0:
#             multiples_of_3.append(num)

#     new_lst.append(multiples_of_3)

# print(new_lst)


# def multiple_of_3(num):
#     return num % 2 == 0

# new_lst = [num for inner_lst in lst
#            for num in inner_lst if num % 3 == 0]

# print(new_lst)


# new_lst = []

# for sublist in lst:

#     sublist = [num for num in sublist if num % 3 == 0]
#     new_lst.append(sublist)

# print(new_lst)


def divisible_by_3(sublist):
    return [num for num in sublist if num % 3 == 0]

new_lst = [divisible_by_3(inner_lst) for inner_lst in lst]
print(new_lst)  