data_set = {1, 2, 3, 4, 5}

# for item in data_set:
#     if item % 2 == 0:
#         data_set.remove(item)

data_set = {num for num in data_set if num % 2 == 0}
print(data_set)


# for loops require a fixed index point: since sets are unordered, iterations
# after the first execution will have no reference point.

# EDIT: you can't change size of set while iteratin gover it......