# input
    - list
# output
    - 2 lists

# rules:
#   explicit:
        - function returns 2 lists:
            - first half in 1st list, 2nd half in 2nd list
        - if list contains odd number of elements, middle element goes in 1st half
#   implicit:
        - lists with 1 element: 2nd list is empty
        - empty list as input: 2 empty lists output


# examples 
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

# data structure
    - lists

# algorithm

1. given input list "lst"
2. set "midpoint_index" to integer that is length of "lst" / 2
3. assign "first_lst" to elements from start to "midpoint_index" of "lst"
4. assign "second_lst" to elements from "midpoint_index" to end of "lst"
5. return a list made up of "first_lst" and "second_lst"
