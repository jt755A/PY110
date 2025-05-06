'''
Problem
Write a function that returns a list of all substrings of a string

    - Rules:
        - Explicit:
            - Substrings are formed by consecutively going through indexes 
            in input:
                - All substrings from index 0 first, then all from index 1 etc
    
        
Examples

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True

Data structures

- (not-quite) Nested lists:
    - each "starting digit" of string will be made up of list of substrings

input: abc    
[
a, ab, abc, ---> index 0
b, bc, --> index 1
'c' --> index 2

These are added iteratively to the final result


Algorithm
1. Given "string"
2. Initialize "result" to an empty list
3. iterate through "starting_char" in "string":
    A. Call "leading_substrings" function on "string" starting 
    index 0 to end of "string"
        - Assign ELEMENTS of resulting list to "result"
    B. call ... on "string" starting at index 1 to end of "string"
        - Assign ELEMENTS of result to "list"

Code

'''

def leading_substrings(string):
    return [string[:idx] for idx in range(1, len(string) + 1)]

# def substrings(string):
#     result = []
    
#     for start_idx in range(len(string)):
#         sublist = leading_substrings(string[start_idx:])

#         # for element in sublist:
#         #     result.append(element)


#         result.extend(sublist)
#         print(result)

#     return result

def substrings(string):
    return [
        substring
        for idx in range(len(string))
        for substring in leading_substrings(string[idx:])                        
    ]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True