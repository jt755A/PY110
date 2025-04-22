# input:
    - string

# output:
    - Dictionary showing percentages of:
        - lowercase, uppercase, "neither" characters in string

# Rules
#   - Explicit:
        - String will always contain at least 1 character
        - percentages returned as STRINGS
            - Rounded to 2 decimal places
        - Percentages should be between 0 and 100

#   - Implicit:
        -

# Examples
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

# Data Structures
    - floats: for percentages
    - dictionaries: to display answer
    - strings...


# Algorithm

1. Given "test_string"
2. Assign length of "test_string" to "str_length"
3. Intialize an empty dictionary called "percentages"
4. Determine relative percentages of lower, upper and neither-case
5. Assign these to "percentages" dictionary
    - Round to 2 decimal places
    - convert to string
6. return "percentages" dictionary