import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])

# "copied" is a shallow copy of the "original" list. Only the topmost layer
# of original is copied: the overall "outer" list.
# The "inner" list objects are shared by both "original" and "copied". 
# Therefore, the indexed element reassignment to "original" affects "copied".
# Since "original" contains nested lists,  In the indexed element reassignment, the object referred to at 