# def reverse_string(string):
#     for char in string:
#         string = char + string

#     return string

# print(reverse_string("hello") == "olleh")

# original function is reassigning variable 'string' to new string in each
# iteration: concatenating "char" with "string" (originally passed in line 1)
# results in 'ellohhello'



# def reverse_string(string):
#     return string[::-1]



def reverse_string(string):
    reversed_string = ''
    for char in string:
        reversed_string = char + reversed_string

    return reversed_string 

print(reverse_string("hello") == "olleh")