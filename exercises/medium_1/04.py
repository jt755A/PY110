'''
Problem
Create a function that will emulate a stack-and-register language, in Python

    Inputs:
        - A string of commands

    Output:
        - No return value: just side effects

    Rules:
        - Explicit:
            - 'Stack' and 'register' are a list and variable initialized to 
            [] and 0.
            - 'Operations' are made upon stack and register: mutating.
            - No return value
            - a number as input means: add this 
            - All operations are integer based

        - Implicit:
            - No return value: just side effects
            - Arguments will not throw errors


Examples

minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)

Data Structures

Lists: The input string needs to be considered word by word.
        - each "word" is an operation/command




Algorithm

1. Intiailize 'stack' to empty list, 'register' to 0
2. Given, "program" input to function
3. Split "program" into each "word"
4. Iterate through each word and carry out the appropriate operation.

n:
1. Test to see if "word" is an integer
    - if yes, convert to an integer and reassign result to "register"

PUSH:
1. Append "register" value to "stack"

ADD:
1. Pop last value of "stack"
2. Reassign "register" to current value of "register" plus popped item

SUB:
As above, change step 2 to... minus popped item

MULT:
As above, change step 2 to... multiply popped item

DIV: 
As above, change step 2 to... divide popped item
1. Ensure that this is INTEGER division

REMAINDER:
As above, change step 2 to... divide popped item
1. Ensure that this is INTEGER remainder

POP:
1. Remove last element of "stack"
2. Reassign "register" to this element

PRINT:
1. print the current value of "register"






Code

'''

def minilang(program):
    COMMAND_LST = ['PUSH', 'ADD', 'SUB', 'MULT', 'DIV', 'REMAINDER', 'POP',
                   'PRINT']
    
    stack = []
    register = 0

    commands = program.split()

    # print(f'the commands in program are: {commands}')

    for command in commands:
        try:
            register = int(command)                            
            
        except ValueError:
            match command:
                case 'PUSH':
                    stack.append(register)
                case 'ADD':
                    register += stack.pop()
                case 'SUB':
                    register -= stack.pop()
                case 'MULT':
                    register *= stack.pop()
                case 'DIV':
                    register //= stack.pop()
                case 'REMAINDER':
                    register %= stack.pop()
                case 'POP':
                    try:
                        register = stack.pop()

                    except IndexError:
                        print('Empty stack condition: You must push '
        'an item to the stack before popping.')
                        return
                        
                case 'PRINT':
                    print(register)
                case _:
                    return f'Invalid operation: {command} - please try again'

print(minilang('HELLO'))


        

# minilang('PRINT')
# 0

# minilang('5 PUSH 3 MULT PRINT')
# # 15

# minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# # 5
# # 3
# # 8

# minilang('5 PUSH POP PRINT')
# # 5

# minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# # 5
# # 10
# # 4
# # 7

# minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# # 6

# minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# # 12

# minilang('-3 PUSH 5 SUB PRINT')
# # 8

minilang('6 PUSH')
# # (nothing is printed)  


        

        

