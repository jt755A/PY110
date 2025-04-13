# input:
    - list of numbers
# output:
    - list of numbers

# rules:
#   -Explicit:
        - lists are made of numberrs
        - input and output lists have same number of members
        - output list made up of running tally from original list

#   -Implicit:
        - input lists with 1 element return that same value
        - empty input list returns an empty input list

# Examples
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True


# Data Structures
    - lists as input and output


# Algorithm

1. given "numbers" list as input
2. initialize variable "current_tally" to zero
4. initialize variable "result_list" to empty list
3. for each "element" of "numbers"
    - add "element" to current value of "current_tally"
    - append value of "current_tally" to "result_list"
4. return "result_list"
