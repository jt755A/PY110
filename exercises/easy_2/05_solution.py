'''
Problem
    - INputs:
        - 2 lists

    - Output:
        - A NEW list with alternating elements from input lists

# Rules
    - Explicit:
        - list1 first, then list2
        - Lists are non-empty
        - Lists have same number of elements

Examples
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

Data structures
    - lists for inputs
    - 

Algorithm

1. Given "list1" and "list2"
2. Create empty list "result"
3. Iterate through both lists, adding element for each to "result"
(ensure that list1, list2 have same length) 


'''

def interleave(lst1, lst2):
    result = []

    # if len(lst1) == len(lst2):
    #     for idx in range(len(lst1)):
    #         result.append(lst1[idx])
    #         result.append(lst2[idx])
    
    # return result

    # zipped_lst = zip(lst1, lst2)
    # for pair in zipped_lst:
    #     for element in pair:
    #         result.append(element)
        
    # return result

    return [element for pair in zip(lst1, lst2)
            for element in pair]

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True