import copy

def rotate_list(my_list):
    if not isinstance(my_list, list):
        return None
    
    # if len(my_list) <= 1:
    #     return my_list
    
    # new_lst = copy.deepcopy(my_list)

    # result = []

    # index = enumerate(new_lst)


    # for idx, value in index:
    #     if idx == 0:
    #         first_value = value
    #     else:
    #         result.append(value)
            
    # result.append(first_value)

    # return result

    if len(my_list) == 0:
        return []
    
    return my_list[1:] + [my_list[0]]
    

      
print(rotate_list(1))
print(rotate_list(None))


print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])