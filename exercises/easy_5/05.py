'''


Rules:
    - Explicit:
        - Input lists are the same length
        - return a new list

# Data structure
    - Ranges: both lists are same length, can index into both
    using index from 1 range.

# Algorithm

1. Given "lst1", "lst2"
2. Iterate through each member of "lst1", "lst2"
    A. At each "idx" in members of both lists:
        - multiply element in "lst1" by element in "lst2"
        - add this result to a new "output_lst"
3. return "output_lst"
'''


def multiply_items(lst1, lst2):
    # return [lst1[idx] * lst2[idx] for idx in range(len(lst1))]

    return [num1 * num2 for num1, num2 in zip(lst1, lst2)]


list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b))# == [4, 10, 18]) # True