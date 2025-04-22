def sequence(integer):
    result = []
    # for num in range(1, integer + 1):
    #     result.append(num)

    # result.extend(range(1, integer + 1))
           
    # return result

    # return [num for num in range(1, integer + 1)]

    return list(range(1, integer + 1))





print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True