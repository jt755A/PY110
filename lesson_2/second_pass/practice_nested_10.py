import random

chars = '0123456789abcdef'
section_lengths = [8, 4, 4, 4, 12]

def random_string(length):
    # result_string = ''
    # for _ in range(length):
    #     result_string += random.choice(chars)

    result_string = ''.join([random.choice(chars) for _ in range(length)])

    return result_string

def generate_uuid():
    uuid_lst = [random_string(section_length) for section_length in section_lengths]
    return '-'.join(uuid_lst)
    

print(generate_uuid())