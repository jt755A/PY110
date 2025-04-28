'''
Problem
Create function with 2 list arguments (each contains numbers). Multiply
number in 1st list by number at same position in 2nd list. Add this number
to a NEW list. Return that new list.

    -Inputs:
        - 2 lists, contain numbers
    - output:
        - 1 new list

# Rules
    Explicit:
        - Multiply elements of input lists together, add to new list
        - Lists have same number of elements
    Implicit:
        - Don't mutate original list

# Examples
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

# Data Structures
    - lists for inputs, output

# algorithm

1. Given "lst1" and "lst2" as inputs
2. Initialize "result" to empty list
3. For each "index" in lst, multiply "element" in "lst1" by "element" in "lst2"
at that "index".
    - Add this new number to "result"
4. Return "result"

   
'''

def multiply_list(lst1, lst2):
    result = []
    # for idx in range(len(lst1)):
    #     result.append(lst1[idx] * lst2[idx])
    
    # return result

    # zipped_lst = zip(lst1, lst2)
    # for pair in zipped_lst:
    #     result.append(pair[0] * pair[1])

    # return result

    # return [pair[0] * pair[1] for pair in zip(lst1, lst2)]
    return [a * b for a, b in zip(lst1, lst2)]


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True