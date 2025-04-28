'''
Problem:
    Input:
        - A list of positive integers

    Output:
        - a string of digits: rounded to 3 decimal places

# Rules
    - Explicit:
        - elements in input are positive integers
        - elements are multiplied together, then divided by number of elements,
        rounded to 3 decimal places, returned as a string

    - Implicit:


Examples/Test Cases

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

Data Structures

- Integers: a running total

Algorithm
1. Given "num_list" input
2. Initialize "product_total" to 1, 
"lst_length" to number of elements in "num_list"
3. Iterate through "num_list", multiply each "num" by "product_total"
    - Assign new total to "product_total"
4. Divide "product_total" by "lst_length"
5. Round answer to 3 decimal places, return as string

'''
def multiplicative_average(lst):
    product_total = 1
    lst_length = len(lst)

    for num in lst:
        product_total *= num
    
    average = product_total / lst_length
    return f'{average:.3f}'

print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")