matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened_matrix = [cell for row in matrix
                         for cell in row]
print(flattened_matrix)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


test = [hello for row in sublist
                