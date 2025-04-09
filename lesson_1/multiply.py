my_numbers = [1, 4, 3, 7, 2, 6]

def multiply(numbers, multiplier):
    multiplied_nums = []

    for current_num in numbers:
        multiplied_nums.append(current_num * multiplier)
    
    return multiplied_nums

print(multiply(my_numbers, 3))