def rotate_rightmost_digits(number, count):
    number_string = str(number)
    digit_lst = list(number_string)
    
    removed_digit = digit_lst.pop(count)

    digit_lst += removed_digit
    return int(''.join(digit_lst))


def max_rotation(number):
    string_num = str(number)

    for idx in range(len(string_num)):
        string_num = rotate_rightmost_digits(string_num, idx)

    return string_num

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True