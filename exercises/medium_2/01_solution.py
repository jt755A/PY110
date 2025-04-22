def letter_percentages(s):
    percentages = {}
    
    string_length = len(s)

    lower_count = 0
    upper_count = 0
    neither_count = 0

    for char in s:
        if char.islower():
            lower_count += 1
        elif char.isupper():
            upper_count += 1
        else:
            neither_count += 1

    percentages['lowercase'] = f'{(lower_count / string_length) * 100:.2f}'
    percentages['uppercase'] = f'{(upper_count / string_length) * 100:.2f}'
    percentages['neither'] = f'{(neither_count / string_length) * 100:.2f}'

    return percentages





expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}

print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)