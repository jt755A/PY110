def repeater(str):
    # result = ''
    
    # for char in str:
    #     result += char * 2
    
    # return result

    return ''.join([char * 2 for char in str])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True