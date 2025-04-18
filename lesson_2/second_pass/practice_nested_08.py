dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}


# result = []

# for food in dict1.values():
#     fruit_colors = []
    
#     if food['type'] == 'fruit':
#         for color in food['colors']:
#             fruit_colors.append(color.title())
        
#         result.append(fruit_colors)

#     if food['type'] == 'vegetable':
#         result.append(food['size'].upper())

# print(result)

        
# food_dict = dict1.values()
# new_result = []

def transform_item(item):
    if item['type'] == 'fruit':
        return [color.title() for color in item['colors']]
    
    elif item['type'] == 'vegetable':
        return item['size'].upper()
    

new_result = [transform_item(food) for food in dict1.values()]
print(new_result)

