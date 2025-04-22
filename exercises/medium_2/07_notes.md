# input:
    - a list of same type, comparable elements


# output
    - returns sorted list

# Rules
#   - Explicit:
        - Sort in place: list mutated in each swap
        - ascending order
        - completed when whole "pass" completed without any swaps

#   - Implicit
        - 

# Examples

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True

# Data Structures

- Outer Loop:
    - Iterates through elements until no "swaps" are made
        - i.e. when the list is sorted in ascended order
- Inner loop:
    - looping through elements in list
        - swapping element if 1st object > 2nd object



# Algorithm

1. given input "lst"
2. Set outer loop to iterate through "elements" in "lst" until "result" equals
an ascending sorted list.
3. Set inner loop to compare "elements"
    A. set "current_value to 0