'''
Problem
Create function that counts number of instances of an element in a list.
After counting, print the element and the count of times it appears in list

#Rules
    Explicit:
        - Elements are case-sensitive
        - total count of element listed alongside element

    Implicit
        - Element printed in order they FIRST appear in list

Examples
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)

Data Structures
- A set to keep track of which elements have already been encountered
- the input list

# Algorithm
1. Given "input" list
2. Assign an empty set to "seen"
3. Print "element" in "input", plus the total count of "element" in "input"
    - print "element" IF it is not already in "seen"
        - Print number of occurences
        - add "element" to "seen"

'''

def count_occurrences(objects):
    seen = set()
    # for element in objects:
    #     if element not in seen:
    #         print(f'{element} => {objects.count(element)}')



    objects_lower = [element.casefold() for element in objects]
    
    for item in objects_lower:
        if item not in seen:
            print(f'{item} => {objects_lower.count(item)}')
            seen.add(item)



vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)