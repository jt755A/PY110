Prompt:
You have a number of building blocks that can be used to build a valid structure. There are certain rules about what determines a valid structure:

The building blocks are cubes.
The structure is built in layers.
The top layer is a single block.
A block in an upper layer must be supported by four blocks in a lower layer.
A block in a lower layer can support more than one block in an upper layer.
You cannot leave gaps between blocks.
Write a program that, given the number of available blocks, calculates the number of blocks left over after building the tallest possible valid structure.


P: understand the Problem

input: a number that represents number of available blocks
output: a number representing leftover blocks, after building tallest possible 'valid' structure

rules:
    Explicit:
        - building blocks are cubes
        - structure bult in layers
        - top layer is single block
        - block in upper layer supported by 4 blocks in lower layer
        - block in lower layer CAN support more than one block in upper layer
        - no gaps between blocks

    Implicit:
        - cube is 3 dimensional object ---> equal length in each dimension
        - bottom face of cube must be supported by 4 blocks in layer below
        #- smallest possible valid structure is 1 block, in 1 layer
        #    - next is: 1 block in top layer, AT LEAST 4 blocks below
        #        - then 4 below.... etc

        - Layer number correlates with blocks in a layer
        - number of blocks in a lyer is layer number * layer number


Questions:
    - How does supporting function work? Does each subsequent lower layer require more blocks than above?
        - Or can descending layers of 4 blocks be used?
    - inputs will be integers?
        - i.e. no partial blocks

    - EDIT: will there always be blocks left over?
        - Answer from examples: NO, but there can be leftover blocks
    = EDIT: Is lower block valid if it has more blocks than it needs?
        - Answer: apparently not, 'unnecessary' blocks are unused


    E: Examples/test cases

print(calculate_leftover_blocks(0) == 0)  # True
    Empty case is valid input
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
    'Unnecessary' blocks not used: they are 'leftover'
print(calculate_leftover_blocks(14) == 0) # True

    D: Data Structures

just integers? - 
    creating a tally, and subtracting necessary blocks per layer

    Comes down to: do you need to *represent* the structure as data?

Or using nested lists:

[
    ['x'],
    ['x', 'x', 'x', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ...
]

A: alogrithm

- given a number of blocks

- 1. set variable 'available_blocks_remaining' to an integer of input number
- 2. create a valid layer
    - set 'layer_number' to 1
- 3. subtract last layer in step 2 from 'available_blocks_remaining'
- 4. repeat steps 2 & 3 until no further valid layers can be created
    - i.e. next layer <= 0
- 5. Calculate 'leftover_blocks': input - 'available_blocks'
- 6. Return 'leftover_blocks'


Problem: Create a valid layer

- Rules:
    - layer is integer number

implicit:
    - number of blocks of layer = square of layer #

    input: layer number (e.g. 1, 2, 3)
    output: layer number * layer number (e.g. 1, 4, 9 etc)





iteration counter = 1
row number = iteration counter
create row
- set available blocks to a variable
    - create a valid layer of blocks
    - subtract number of blocks used from avail. block variable above
