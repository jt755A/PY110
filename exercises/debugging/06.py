def multiply_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(multiply_sum(numbers, 2) == 20)

# the function defined in line 1 shadows the built in Python function 
# also named sum. Renaming to sum_ fixes the issue

