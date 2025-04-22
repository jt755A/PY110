def sum_square_difference(count):
    my_count = range(1, count + 1)
    sum_of_count_squared = sum(my_count)**2
    squares_of_count = sum([number**2 for number in my_count])

    return sum_of_count_squared - squares_of_count


print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True