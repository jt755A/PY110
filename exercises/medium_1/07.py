'''
Create a function that returns an integer representing the 'nth'
fibonacci number

Input:
    - an integer: an index to the fibonacci sequence

Output:
    - an integer: the nth number in sequence

Rules
    - Explicit:
        - nth number in sequence is the sum of 2 previous numbers:
            - n-1, + n-2

    - Implicit:
        - 1st and 2nd number are given, simple rule follows for all subsequent
            - 1st and 2nd should have separate clause
        - when n > 2:
            number of elements in "sublist" will equal n
            - Result is last number in list
        - input is greater than 0, and integer

Examples

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

Data Structures

Lists: list will be constructed UP TO number supplied as input:

e.g. 
    - fibonacci(3): [1, 1, 2] = 2
    - fibonacci(4): [1, 1, 2, 3] = 3
    - fibonacci(5): [1, 1, 2, 3, 5] = 5

    
Algorithm

1. Initialize "fibonacci_seq" to [1, 1]
2. Given "number"
3. If "number" is less than equal to 2:
    - pull from "fibonacci_seq"
4. Construct a full list of numbers in sequence, updating "fibonacci_seq"
    - A while length of "fibonacci_seq" less than "number"
        - iterate over "fibonacci_seq" adding last 2 numbers together:
            - assign to "current_fibonacci_number"
            - Append to "fibonacci_seq"
        -
    - B...
5. Return last number of "fibonacci_seq"

'''

def fibonacci(number):
    fibonacci_seq = [1, 1]
    if 1 <= number <= 2:
        return fibonacci_seq[number - 1]
    
    while len(fibonacci_seq) < number:
        latest_num = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(latest_num)
    
    return fibonacci_seq[-1]
    
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

