def is_palindrome(input_string):
    reversed_input = input_string[::-1]
    return input_string == reversed_input

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)
print(is_palindrome('Madam') == False)
print(is_palindrome("madam i'm adam") == False)