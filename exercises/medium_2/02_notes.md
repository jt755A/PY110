# input:
    - 3 numbers: sides of triangles as arguments

# output:
    - a string saying the type of triangle the inputs generate:
        - Equilateral
        - Isoceles
        - Scalene
        - Invalid

# Rules
    - All lengths are numbers
    - Triangle is invalid if:
        - Sum of two shortest lengths must be greater than longest side.
        - Every side must be greater than 0

#   - Implicit:
        - Order arguments are listed doesn't matter

# Examples

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

# Data structures

- Lists: to sort arguments in ascending order
- floats otherwise

# Algorithm

1. given 3 inputs: "side1, side2, side3"
2. if any side is <= 0:
    - Return "invalid"
3. create "ordered_lst": 3 sides in ascending order
4. Unpack to 3 variables:
    - shortest
    - middle
    - longest

5. If "shortest" equals "middle" AND "middle" equals "longest":
    - return "equilateral"
6. if "shortest" + "middle" < "longest"
    - return "invalid"

7. Return "isoceles" if any of following are true:
    - "side1" equals "side2"
    - "side1" equals "side3"
    - "side2" equals "side3"




