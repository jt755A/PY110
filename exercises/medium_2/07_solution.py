# def bubble_sort(lst):
#     while lst != sorted(lst):
#         counter = 0
        
#         while counter < len(lst) - 1:
#             if lst[counter] > lst[counter+1]:
#                 lst.insert(counter, lst.pop(counter+1))

#             counter += 1
        
#     return lst

def bubble_sort(lst):
    while True:
        swapped = False
        for idx in range(1, len(lst)):
            if lst[idx - 1] <= lst[idx]:
                continue
        
            lst[idx - 1], lst[idx] = lst[idx], lst[idx - 1]
            swapped = True

        if not swapped:
            break





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