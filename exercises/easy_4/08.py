'''
Problem:
return a list containing all palindromic substrings from string input.
In the order that they appear in original

    - Rules:
        - Explicit:
            - "palindrome" is string that reads the same forward and backwards
            - case matters
            - special characters matter
            - single characters are NOT palindromes
            - Include duplicate palindromes, if present

        - Implicit:
            - if no palindromes in string, return an empty list
            - remove whitespace from input


Examples

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True


Data Structures

Calling "substrings" function will give a list of all substrings

Select only substrings that are palindromic


Algorithm

1. given "string"
    - remove whitespace
2. assign "all_substrings" to result of calling "substrings" function on 
"string" (a list)
3. Return a new list that contains only palindromes
    - Create an "is_palindrome" helper function
    - Iterate through each "substring" in "all_substrings"
        - if it's a palindrome: select in list
Code

is_palindrome:

Rules: 
IF length greater than 1
 AND "substring" reads forwards and backwards identically


'''


def leading_substrings(string):
    return [string[:idx] for idx in range(1, len(string) + 1)]


def substrings(string):
    return [
        substring
        for idx in range(len(string))
        for substring in leading_substrings(string[idx:])
    ]

# def palindromes(string):
#     all_substrings = substrings(string.replace(' ', ''))
    
#     palindromes = [substring for substring in all_substrings
#             if len(substring) > 1
#             if substring[:] == substring[::-1]
#     ]

#     # print(palindromes)
#     return palindromes

# def palindromes(string):
#     return [substring for substring in substrings(string.replace(' ',''))
#             if len(substring) > 1
#             if substring[:] == substring[::-1]
#     ]


def is_palindrome(word):
    return len(word) > 1 and word[:] == word[::-1]

def palindromes(string):
    return [substring for substring in substrings(string)
            if is_palindrome(substring)]


print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True