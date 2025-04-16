# input: dictionary

# output:
    - return dict

# rules:
    - Explicit:
        - function "inverts" dict:
            - keys become values
            - values become keys

# Examples

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

# Data structures
    - Dicts
    - comprehension


# Algorithm

1. given "my_dict"
2. Iterate through each "element" of "my_dict"
    - for each "key", "value" in "my_dict":
        - assign to a new "reversed_dict" in reverse

3. return "reversed_dict"