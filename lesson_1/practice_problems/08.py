statement = "The Flintstones Rock"


letter_frequency = {}

# unique_letters = set(statement)

# for char in unique_letters:
#     letter_frequency[char] = statement.count(char)

# print(letter_frequency)

statement = statement.replace(' ', '')

# for letter in statement:
#     letter_frequency[letter] = statement.count(letter)


for letter in statement:
    letter_frequency[letter] = letter_frequency.get(letter, 0) + 1

print(letter_frequency)