def swap_name(name):
    name_list = name.split()
    first_name, last_name = name_list
    return f'{last_name}, {first_name}'

# swap_name('hello world')

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True