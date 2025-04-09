def double_odd_index(numbers):
    doubled_numbers = []
    
    for current_num in numbers:

        if numbers.index(current_num) % 2 == 1:
            doubled_numbers.append(current_num * 2)
        else:
            doubled_numbers.append(current_num)
            
    return doubled_numbers


my_numbers = [1, 4, 3, 7, 2, 6]

print(double_odd_index(my_numbers))
print(my_numbers)