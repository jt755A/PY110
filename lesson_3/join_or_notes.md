# Problem:
#    input:
        - A list
        - 2 potential default parameters:
            - delimiter
            - 'joining word'

#   output:
        - a string containing elements in input, using 'or' to connect last
        2 elements
            - unless additional parameters are used

# Rules
#   Explicit:
        - last 2 elements in input are connected with or
        - comma used to separate other elements

#   Implicit:
        - unless otherwise specificed:
            - 'or' is joining word
            - ', ' is delimiter
        
        - return empty string if input is empty list
        - return just the element as string if 1 element
        - if 2 elements in input:
            no delimiter, just joining word

# Examples

print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"

# Data structure
    - list comprehension?
        to connect elements BEFORE last element

    - strings

# Algorithm
1. set default parameters:
    - delimiter
    - joining word
2. given "lst" as input
3. for each "element" in "lst", convert to a string and add to empty list
"str_lst"
4. Join Elements:
    A. Determine how many times to iterate through "str_lst":
       - if length of "str_lst" is <= 1:
            - skip to step 5
        - if length of "str_lst" is 2:
            - connect using "joining_word"
        - else: connect using "delimiter" and "joining_word"

# Sub function:
