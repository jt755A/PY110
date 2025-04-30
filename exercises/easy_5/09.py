'''
Problem
Write a function taking a string as input, returning a new string with
every other character capitalized (non-alphabetic characters are unchanged,
and are excluded in the "count" for alternating.)

Input:
    - A string

Output:
    - new string: alternating capitalization

Rules:
    Explicit:
        - Capitalize starting with 1st character, 3rd etc
        - next character should be lowercase
        - Non-alpha characters are unchanged
        - non-alpha characters (including spaces) not included in alternating
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
2. Get an "index" for each "char" in "string_seq"
3. intialize variable "alpha_count" to 0
4. Iterate through each "char" in "string_seq"
    A. if "char" isn't alphabetic: add to "result"
    B. If it is:
        If "alpha_count" is an even number:
            - capitalize "char" and add to "result"
            - increment "alpha_count" by 1
        if "alpha_count" odd:
            - lowercase "char" and add to "result"
            - increment "alpha_count" by 1

5. return "result"


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
    result = ''
    alpha_count = 0

    # for idx in range(len(string_seq)):
    #     if string_seq[idx].isalpha():
    #         result += (string_seq[idx].upper() if alpha_count % 2 == 0
    #                    else string_seq[idx].casefold())
    #         alpha_count += 1
        
    #     else:
    #         # for non-alpha characters
    #         result += string_seq[idx]
    
    # return result

    for char in string_seq:
        if char.isalpha():
            result += char.upper() if alpha_count % 2 == 0 else char.casefold()
            alpha_count += 1
        else:
            result += char

    return result

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

