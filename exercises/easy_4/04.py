def sort_key(item):
    return item[1]

def order_by_value(dictionary):
    sorted_items = sorted(dictionary.items(), key=sort_key)
    return [key for key, value in sorted_items]


my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']



print(order_by_value(my_dict) == keys)  # True