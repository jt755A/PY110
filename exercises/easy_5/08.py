'''
Problem
Write a function taking a string as input, returning a new string with
every other character capitalized (non-alphabetic characters are unchanged,
but are included in the "count" for alternating.)

Input:
    - A string

Output:
    - new string: alternating capitalization

Rules:
    Explicit:
        - Capitalize starting with 1st character, 3rd etc
        - next character should be lowercase
        - Non-alpha characters are unchanged
        - non-alpha characters (including spaces) included in alternating
        scheme

    Implicit: empty string as input, returns empty string

Examples

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

Data Structures

Just strings, an in

Algorithm
1. Given "string_seq", initialize "result" to an empty string
2. Iterate through each "character" in "string_seq" capitalizing in alternate
fashion
    A. Check if "character" is alphabetic
    B. If so, capitalize if it falls on an "odd" number in sequence
        - Add to "result" string
    C.  - If not on "odd" number in sequence:
        - Add to "result" string unchanged
    D. If non-alphabetic character:
        - Add to "result" string unchanged
        - 
3. Return "result" 

'''

def staggered_case(string_seq):
    # result = ''

    # for idx in range(len(string_seq)):
        
    #     if string_seq[idx].isalpha():
    #         if idx % 2 == 0:
    #             result += string_seq[idx].upper()
    #         else:
    #             result += string_seq[idx].casefold()
        
    #     else:
    #         # if character is not alphabetic
    #         result += string_seq[idx]
    
    # return result

    return ''.join([upper_or_lower(idx, char) for idx, char in enumerate(string_seq)])
    # for idx, char in enumerate(string_seq):
    #     print(upper_or_lower(idx, char))




def upper_or_lower(index, char):
    if char.isalpha():
        if index % 2 == 0:
            return char.upper()
        else:
            return char.casefold()
    else:
        return char  

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string))# == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True