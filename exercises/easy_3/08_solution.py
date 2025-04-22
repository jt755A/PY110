def sequence(count, number):
    multiples = []
    # for idx in range(1, count+1):
    #     multiples.append(idx * number)

    # return multiples

    return [number * idx for idx in range(1, count + 1)]

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True