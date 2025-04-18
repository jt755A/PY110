def rotate_rightmost_digits(number, count):
    number_string = str(number)
    digit_lst = list(number_string)
    
    last_digit = digit_lst.pop(-count)

    digit_lst += last_digit
    return int(''.join(digit_lst))


    # number_string = str(number)
    # print(number_string[:len(number_string)-count])
    # print(number_string[count+1:count+1])
    # # result = number_string[:len(number_string)-count+1] + number_string[count:]
    # print(result)


print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True