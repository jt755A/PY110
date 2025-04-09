produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(food):
    selected_fruit = {}

    for key, value in food.items():
        if value == 'Fruit':
            selected_fruit[key] = value

    return selected_fruit


print(select_fruit(produce))  # { apple: 'Fruit', pear: 'Fruit' }