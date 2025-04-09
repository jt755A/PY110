ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

age_tally = 0
for age in ages.values():
    age_tally += age

print(age_tally)


total_age = sum(ages.values())