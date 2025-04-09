def calculate_leftover_blocks(available_blocks):
    available_blocks_remaining = available_blocks
    current_layer_number = 1

    while available_blocks_remaining > -1:    
        
        blocks_required_current_layer = current_layer_number**2

        if available_blocks_remaining >= blocks_required_current_layer:
            available_blocks_remaining -= blocks_required_current_layer
            current_layer_number += 1
        
        else:
            break
            
    return available_blocks_remaining



print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True