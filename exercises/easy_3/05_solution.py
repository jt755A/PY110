def reverse_number(integer):
    str_integer = str(integer)
    reverse_string = str_integer[::-1]
    return int(reverse_string)

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True