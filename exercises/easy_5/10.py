'''
Problem
Create function that Removes consecutive integers from a sequence. return refined sequence
# Input:
    A list of integers

# output:
    new list of integers, consecutive duplicates removed

# Rules:
    - no consecutive integers

    # Implicit:
        It's unclear whether the integers have to be consecutive, or just
        duplicates to be filtered out: test case doesn't show

Example

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

Data structures
- lists

Algorithm (just for removing duplciate)

1. given "input_lst"
2. Initialize "seen" to empty set, "result" to empty list
3. Iterate through elements in "input_lst":
    - If "element" not in seen":
        - append to "result"
        - add "element" to "seen"
    - If "element in "seen":
        - continue to next "element"
4. return "result"


For consecutive duplicates

1. Given "orig_numbers" list
2. Initialize "result" to empty list
3. add first element of "orig_numbers" to "result"
4. Iterate through the rest of "orig_numbers":
    A. If "element" in "orig_numbers" does NOT equal previous
    number:
        - Add to "result"
5. Return "result"
'''

def unique_sequence(orig_numbers):
    # result = []
    # seen = set()

    # for number in orig_numbers:
    #     if number not in seen:
    #         result.append(number)
    #         seen.add(number)
        
    # return result

    result = []
    result.append(orig_numbers[0])

    for element in range(1, len(orig_numbers)):
        if orig_numbers[element] != orig_numbers[element - 1]:
            result.append(orig_numbers[element])
        
    return result

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True