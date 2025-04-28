'''
create a memoization version of a recursive Fibonacci sequence

Input:
    - nth number of sequence to find

Output
    - That number

Rules
    - Implicit:
        - Previous value of fibonacci sequence (starting from 2) is saved into
        data structure once it is calculated

Examples
print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True
    
# Data Structures

fibonacci_dict = {}
1st iteration: {1: 1}
second: {1: 1, 2: 1}
3rd: {1: 1, 2: 1, 3: 2}
4th: 
{
1: 1,
2: 1,
3: 2,
4: 3
}

Algorithm

1. Intialize first two values of Fibonacci sequence to as values to
"fibonacci_dict"; key is nth number
2. For each iteration, try to access values at (n-1) and (n-2) in
"fibonacci_dict"
    - If can't.....
3. Add these values together: append to "fibonacci_dict" - iteration: result
4. return "result"


'''

def fibonacci(nth):
    memo = {}

    if nth <= 2:
        memo[nth] = 1
        return memo[nth]

    memo[nth] = (memo.get(nth - 1, fibonacci(nth - 1))
    + memo.get(nth - 2, fibonacci(nth - 2)))

    return memo[nth]

    # fibonacci_dict[nth] = (fibonacci_dict.setdefault(nth - 1, fibonacci(nth - 1))
    #                        + fibonacci_dict[nth - 2])

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True