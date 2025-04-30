'''
Problem
Transpose an MxN matrix, without mutating original matrix

Input:
    - A nested list

Output:
    - A transposed nested list

Rules:
    - Explicit:
        - Tranpose MxN matrix, to NxM columns by rows
        - Don't mutate Original matrix
    - Implicit:
        Input always contains nested list

Examples

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)

Data Structures

transpose([[1, 2, 3, 4]]) becomes [[1], [2], [3], [4]]
single NESTED list becomes 4 individual nested lists





Nested Lists

Algorithm

1. Given "matrix"
2. Determine number of "input_rows" (this will become output columns)
    - i.e. number of nested lists
3. Determine number of "input_columns" )this will become output rows)
    - i.e. the length of ANY nested list in input
4. Build list of empty nested lists:
    - using "input_columns" for number
5. Initialize "output_rows" to "input_columns", "output_columsn" to "input_rows"
6. Populate nested inner lists
    - for each "nested_lst" take "output_columns" number of elements, 

C
'''

def transpose(matrx):
    # input_rows = len(matrx)
    # input_cols = len(matrx[0])

    # output_rows, output_cols = input_cols, input_rows

    # transposed = []

    # for _ in range(output_rows):
    #     transposed.append([])

    # for row in range(output_rows):
    #     for col in range(output_cols):
    #         transposed[row].append(matrx[col][row])

    # return transposed

    new_matrix = [[] for _ in range(len(matrx[0]))]
    print(new_matrix)

    col_idx = 0

    while col_idx < len(matrx):

        for row in matrx:
            new_matrix[col_idx].append(row[col_idx])

        col_idx += 1

    return new_matrix
            


# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)