ROUND = ['1st', '2nd', '3rd', '4th', '5th', 'last']

def ask_for_number(i):
    return input(f'Enter the {ROUND[i]} number: ')

def searching():
    user_nums = []
    
    for idx in range(len(ROUND) - 1):
        num = int(ask_for_number(idx))
        user_nums.append(num)

    last_num = int(ask_for_number(-1)) # retrieves 'last' from ROUND

    result_lst = ','.join([str(element) for element in user_nums])

    if last_num in user_nums:
        print(f'{last_num} is in {result_lst}.')
    
    else:
        print(f"{last_num} isn't in {result_lst}.")

searching()



