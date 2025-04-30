def transpose(matrx):
 

    new_matrix = [[] for row in matrx]

    col_idx = 0

    while col_idx < len(matrx):

        for row in matrx:
            new_matrix[col_idx].append(row[col_idx])

        col_idx += 1

    # print(matrx)
    # print(new_matrix)
    return new_matrix
            


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True