import random

UUID_CHARS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              'a', 'b', 'c', 'd', 'e', 'f']

PATTERN_LENGTHS = [8, 4, 4, 4, 12]

def section(length):
    result = ''
    for _ in range(length):
        result += str(random.choice(UUID_CHARS))
    return result

def append_dash(text):
    return text + '-'

def generate_UUID():
    end_result = ''
    
    for pattern in PATTERN_LENGTHS:
        end_result += section(pattern)
        end_result = append_dash(end_result)
    
    return end_result.rstrip('-')

    return end_result


print(generate_UUID())


