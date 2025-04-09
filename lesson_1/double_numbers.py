my_numbers = [1, 4, 3, 7, 2, 6]

def double_numbers(numbers):
    for idx in range(len(numbers)):
        numbers[idx] *= 2

    return numbers

print(double_numbers(my_numbers))
print(my_numbers)