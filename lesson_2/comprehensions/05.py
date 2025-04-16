lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_odd_members(sublist):
    odd_nums = [num for num in sublist if num % 2 == 1]
    return sum(odd_nums)

new_lst = sorted(lst, key=sum_odd_members)
print(new_lst)