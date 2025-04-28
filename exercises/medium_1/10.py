'''
Input:
    - Integer greater than 2

Data Structures

Will make fibonacci procedurally (for processing time)

To find index of nth digit:
    - Ranges: from 1 to length of fibonacci sequence
    - convert digit to string version

# Algorithm

1. given "digit_length"
1. Using previous procedural fibonacci program
2. Iterate from "idx" 1 upwards to "digit_length" + 1:
    A - in each iteration, check if a string representation of
    last number in sequence has a length of "digit_length"
    B: If it doesn't:
        continue
    C. If it does:
        return this "idx" within the general fibonacci sequence

'''

def generate_fibonacci(number):
    fibonacci_seq = [1, 1]
    if number <= 2:
        return fibonacci_seq[number - 1]
    
    while len(fibonacci_seq) < number:
        latest_num = fibonacci_seq[-1] + fibonacci_seq[-2]
        fibonacci_seq.append(latest_num)
    
    return fibonacci_seq[-1]

def find_fibonacci_index_by_length(digits):
    fibonacci_lst = []
    counter = 1

    while True:
        fibonacci_lst.append(generate_fibonacci(counter))
        # print(counter, fibonacci_lst)

        if len(str(fibonacci_lst[-1])) == digits:
            return counter
            # break

    
        counter += 1

    # print(f'final: {counter}, {fibonacci_lst}')
    # return counter

print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
# print(find_fibonacci_index_by_length(1000) == 4782)