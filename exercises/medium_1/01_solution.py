def rotate_list(my_list):
    if not isinstance(my_list, list):
        return None
    
    if my_list == []:
        return my_list
    
    rotated_lst = []
    rotated_lst.append(my_list[1:])
    rotated_lst.append(my_list[0])

    return rotated_lst
                         
    
print(rotate_list([1, 2]))
print(rotate_list(None))