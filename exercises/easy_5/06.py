'''
Problem
Write a function taking a list of numbers. This list is processed to
create "leading subsequences" for each element in the list. Each subsequence
is summed. All of these sums are themselves summed. The result is returned.

# Input:
    - list of numbers

# ouput:
    - an integer representing sum of sums of "leading subsequences" in input

# Rules:
    - Explicit:
        - the input least contains at least one number
    
    - Implicit:
        - A "leading subsequence" is (1st element)



Examples

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True

# Data structures
    - Nested lists to represent leading subsequences
input: [3, 5, 2] becomes [3], [3, 5], [3, 5, 2]

    Range for subsequence:
        - Start from 0 in each iteration
        - Go to 'idx' + 1 in each
idx in range(length of lst):
lst[0: idx + 1]


Algorithm
1. Given "input_lst"
2. create a "subsequences" list
    A. Iterate through "input_lst"
    B. Each iteration go from beginning of "input_lst" up to each "idx"
3. Sum each "subsequence" in "subsequences"
4. Sum each result from step 3
5. Return number from step 4
'''
def sum_of_sums(num_lst):
    # subsequences = [num_lst[0:idx] for idx in range(1, len(num_lst) + 1)]
    sum_subsequences = [sum(num_lst[0:idx]) for idx in range(1, len(num_lst) + 1)]
    # sums_subsequences = [sum(subsequence) for subsequence in subsequences]
    # return sum(sums_subsequences)
    return sum(sum_subsequences)


print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True