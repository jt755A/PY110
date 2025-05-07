'''
Problem

Merge two SORTED lists, iteratively: no sort function

Input:
    - 2 sorted lists
Output:
    return a NEW sorted list

    Rules:
        - Explicit:
            - No sort functions
            - Don't mutate input lists

Examples
# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)

Data Structures

[1, 5, 9], [2, 6, 8]
becomes: [1, 5, 9, 2, 6, 8]

iterating:
index 0: 1 < 5: True # do nothing
index 1: 5 < 9: True # do nothing
index 2: 9 < 2: False # insert 2 before 9
.....
End up with a boolean list [True, True, False ....]
When all are true: break out of loop


Lists:
1.Combine two lists into a new one named "result" (don't mutate)
2. Continually iterate through "result" using indexing
3. Compare elements:
    A. Append boolean result of less than OR EQUAL TO comparison between 2 elements
    B. At each iteration, check if current item is GREATER than NEXT item
        - If yes, insert 2nd item BEFORE current item
        - If not, do nothing

4. At end of iterating through all elements, if EVERY comparison is true:
    - Break out of loop

5. Return the 'result" list


A
Code
'''
def merge(lst1, lst2):
    result = lst1 + lst2
    # print(f'lst1: {lst1} lst2: {lst2} result: {result}') # checks for mutating

    while True:
        smaller_than_lst = []
        
        for idx in range(len(result) - 1):
            smaller_than_lst.append(result[idx] <= result[idx + 1])

            if result[idx] > result[idx + 1]:
                result.insert(idx, result.pop(idx + 1))
            # print(f'idx: {idx}, result: {result}')
            
            # print(result)

        # print(smaller_than_lst)
        if all(smaller_than_lst):
            break
    
    return result
            



# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)