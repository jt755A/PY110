'''
Create an average of integers in list. Answer is rounded down
to nearest integer.

Input:
    - A list of positive integers

Output:
    - an integer representing an average

Rules
    - Explicit:
        - input List is never empty
        - elements in input list are all positive integers
        - "integer component" of average is used: round down to nearest
        integer

Examples
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True


Data structures
- Just numerics

Algorithm
1. Given "numbers" list
2. Calculate "sum" of "numbers"
3. Divide Step 2 by number of elements in "numbers"
4. Round Step 3 DOWN to nearest integer
5. return integer from step 4.

'''

def average(numbers):
    return sum(numbers) // len(numbers)

print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True