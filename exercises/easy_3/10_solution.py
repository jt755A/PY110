# def open_parenth_idxs(my_str):
#     return [idx for idx in range(len(my_str)) if my_str[idx] == '(']

# def closed_parenth_idxs(my_str):
#     return [idx for idx in range(len(my_str)) if my_str[idx] == ')']



# def is_balanced(string):
#     if '(' not in string and ')' not in string:
#         return True

#     if string.count('(') != string.count(')'):
#         return False
    
#     open_parenth_lst = open_parenth_idxs(string)
#     closed_parenth_lst = closed_parenth_idxs(string)
#     index_length = len(open_parenth_lst)

#     for idx in range(index_length):
#         if closed_parenth_lst[idx] < open_parenth_lst[idx]:
#             return False
    
#     return True

OPEN_CHARS = ['(', '[', '{']
CLOSED_CHARS = [')', ']', '}']


def is_balanced(s):
    if s.count("'") % 2 != 0 or s.count('"') % 2 != 0:
        return False
    
    open_count = 0

    for char in s:
        if char in OPEN_CHARS:
            open_count += 1
        elif char in CLOSED_CHARS:
            open_count -= 1
        elif open_count < 0:
            return False
    
    return open_count == 0
        

        





print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
print(is_balanced("What []is{} up") == True)      # True
