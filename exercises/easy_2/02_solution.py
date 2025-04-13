def union(arg1, arg2):
    # combined_lst = arg1 + arg2
    # result_set = set(combined_lst)
    # return result_set

    return set(arg1).union(set(arg2))

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True
print(union([], []))