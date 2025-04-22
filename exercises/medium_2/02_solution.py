def triangle(side1, side2, side3):
    side_lengths = side1, side2, side3
    
    for length in side_lengths:
        if length <= 0:
            return "invalid"
    
    if (side1 == side2) and (side2 == side3):
        return "equilateral"    
    
    ascending_lengths = sorted(side_lengths)
    # print(ascending_lengths)
    shortest = ascending_lengths[0]
    middle = ascending_lengths[1]
    longest = ascending_lengths[-1]
    
    if (shortest + middle) <= longest:
        return "invalid"
    
    elif any([side1 == side2, side1 == side3, side2 == side3]):
        return "isosceles"
    
    else:
        return "scalene"
    


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True