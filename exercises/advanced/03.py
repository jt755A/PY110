'''
Problem
Rotate an MxN matrix 90 degrees clockwise, without mutating original matrix

Input:
    - A nested list

Output:
    - A rotated nested list

Rules:
    - Explicit:
        - Tranpose MxN matrix, to NxM columns by rows
        - Don't mutate Original matrix
        - Rotate 90 degrees clockwise
    - Implicit:
        - Input always contains nested list
        - Lenght of each input list is the same?
        - Length of each input row becomes number of nested lists in new matrix
        - number of input rows becomes length of each nested list in new matrix

Examples

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)

Data Structures

rotate90([[1, 2, 3, 4]]) becomes [[1], [2], [3], [4]]
single NESTED list becomes 4 individual nested lists

- Length of each input row becomes number of nested lists in new matrix
- number of input rows becomes length of each nested list in new matrix



Nested Lists

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

First iteration: [5, 3]
Second iteration:[1, 7]
....
Looping UPWARDS for "columns" in input:
    Pull from LAST "row" downwards
        - grab the item at [row][col]
    next "column" repeat....

    

Algorithm

1. Given "matrix"
2. Determine number of "input_rows" (this will become output columns)
    - i.e. number of nested lists in input
3. Determine number of "input_columns" )this will become output rows)
    - i.e. the length of ANY nested list in input
4. Build list of empty nested lists:
    - using "input_columns" for number
# 5. Initialize "output_rows" to "input_columns", "output_columsn" to "input_rows"
6. Populate nested inner lists
    Outer loop: A. Start iterating through "input_columns" from start to end
    B. Inner loop: Start iterating through "input_rows" from end to 

7. Return rotated new matrix
C
'''

def rotate90(matrx):
    input_rows = len(matrx)
    input_cols = len(matrx[0])


    rotated = []

    for _ in range(input_cols):
        rotated.append([])

    # print(rotated)

    for col in range(input_cols):
        for row in range(input_rows - 1, -1, -1):
            rotated[col].append(matrx[row][col])

            print(f'input col = {col}, input row = {row}, {rotated}')
    
    # for row in range(input_rows):
    #     for col in range(input_cols):
    #         rotated[row].append(matrx[col][row])

    return rotated

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2) 