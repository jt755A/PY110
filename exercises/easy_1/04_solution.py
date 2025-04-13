def running_total(numbers):
    current_tally = 0
    result_list = []

    for num in numbers:
        current_tally += num
        result_list.append(current_tally)
    
    return result_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True