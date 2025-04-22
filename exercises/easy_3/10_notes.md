# input:
    - string argument

# output:
    - returns Boolean: True if parentheses in string are "balanced"

# Rules
#   - Explicit:
        - "balanced" means parentheses occur in '(' and ')' pairs
            - must start with a '(', not a ')'

#   - Implicit:
        - If no parentheses, return True
        - if unequal number of ( or ), then False
        - nth ( has to occur BEFORE nth )

# Examples

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

# Data Structures

- List of indexes of '(' within string
- List of indexes of ')' within string
- integers: counting occurences of both parentheses in string

# Algorithm

1. given 'string'
2. Determine if any parentheses are in 'string'
    - If not, return True
    - If so, continue to step 3
3. Determine if there are equal numbers of '(' and ')'
    - If not, return False
    - If so, continue to step 4
4. Determine if each resepective ')' occurs before corresponding ')'
    A. Create 'open_parentheses_idx' list: contains indexes of where '('
occur in string
    B. Create 'closed_parentheses_idx' list: contains indexes of where ')'
occur in string
    C. Iterate through all members in 'open_parentheses_idx' and 
     closed_parenthesis_idx'
        - if all "open..." indexes are < than 'closed...' indexes:
            - Return True
            - Else return False