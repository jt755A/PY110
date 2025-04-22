def is_valid_triangle(smallest, middle, largest):
    return smallest > 0 and smallest + middle + largest == 180

def get_triangle_type(smallest, middle, largest):
    if largest == 90:
        return "right"
    elif smallest < 90 and middle < 90 and largest < 90:
        return "acute"
    elif largest > 90:
        return "obtuse"
        
    
# def get_triangle_type

def triangle(angle1, angle2, angle3):
    total_angle = angle1 + angle2 + angle3
    smallest = min(angle1, angle2, angle3)
    largest = max(angle1, angle2, angle3)
    middle = total_angle - smallest - largest

    if is_valid_triangle(smallest, middle, largest):
        return get_triangle_type(smallest, middle, largest)
    
    else:
        return "invalid"

        
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True