def halvsies(lst):
    if len(lst) % 2 == 0:
        midpoint_index = len(lst) // 2
    else:
        midpoint_index = (len(lst) // 2 ) + 1
    
    first_lst = lst[:midpoint_index]
    second_lst = lst[midpoint_index:]

    return [first_lst, second_lst]




# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])