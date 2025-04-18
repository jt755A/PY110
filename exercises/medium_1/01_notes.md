# Problem

# Input:
    - a list
# output
    - a new 'rotated' list

# Rules

#   - Explicit:
        - 'rotate' a list:
            - first element moves to the end
        - do not modify input list
        - if input is empty list: return the empty list
        - if input is not a list: return None

#   - Implicit
        - lists can contain, dicts, ints, strings, sets etc


# Test Cases

# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])

# Data structures
    - list: must be a deep copy to avoid mutating original?

# Algorithm

1. Determine if "input" is list
    - if not, return None
2. Determine if list is empty:
    - if yes, return "input"
3. make a deep copy of "input": called "new_lst'
4. make an empty list called "result"
5. iterate through "new_lst"
6. map the list 'object' position to an 'index'
7. add all elements from "new_lst" to "result", starting from second "index" 
8. Add first index item to "result"
9. return "result"