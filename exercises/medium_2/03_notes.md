# input:
    - Three angles (in degrees)

# output:
    - a string describing type of triangle, the angles describe

# rules

#   - Explicit:
        - Valid triangle:
            - all angles must add to 180 degrees
            - all angles must be greater than 0
        
        - "right": one angle equals 90
        - "acute": all three angles are less than 90
        - "obtuse" one  angle is greater than 90
        - all angles are integers


# Examples
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

# Data Structures
    - ...

# Algorithm



1. given "angle1", "angle2", "angle3"
2. Determine smallest, middle, longest angle:
    - assign to variables "smallest", "middle", "longest"
    - "middle" = 180 - "smallest" - "longest"

3. Create "is_valid_triangle" helper function
    - takes "smallest", "middle", "largest" angles

4. If "longest" equals 


# get_triangle_type helper function
takes (shortest, middle, longest) as inputs
1. If "longest" equals 90:
    - return "right"
2. if all three angles less than 90 each:
    - return "acute"
3. if any "largest" greather than 90:
    - return "obtuse"