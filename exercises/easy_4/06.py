'''
Problem
Write a function that returns a new list of substrings, shortest
to longest

    - Rules:
        - Explicit:
            - Each substring starts with first letter of word
            - Each subsequent substring 1 character longer than previous


Examples
# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

Data Structures
String manipulation:
- using progresively bigger slices of input string

Algorithm

1. Given "string"
2. Initialize "result" to an empty list
3. Iterate through "string":
    - Pull first character: append to "result"
    - Next iteration: pull first to 2nd characters
        - append to result
    - Continue reach end of "string"
4. Return "result"

C
'''
def leading_substrings(string):
    result = []

    return [string[:idx] for idx in range(1, len(string) + 1)]

    # for idx in range(1, len(string) + 1):
    #     result.append(string[:idx])

    # return result
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])


