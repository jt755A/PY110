'''
Problem
Write a function that returns the number of Friday the 13ths in a 
year that is supplied as an argument

    - Rules:
        - Explicit:
            - Assume year is greater than 1752 (gregorian calendar)
            - Assume this calendar will not change

Examples

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True

Data Structures

Nested Lists?
1. List of dates of all Fridays in a year
2. 2nd list: Filter list 1 for dates where day component is 13th of month



Algorithm

1. given "year"
2. Create "friday_lst" list of all Fridays in "year"
3. Create "friday_13th" list of all "dates" in "friday_lst" that fall on 
13th of the month
4. Return the number of entries in "friday_13th" list

Alternate

1. given "year"
2. Iterate through each "month" in "year"
3. create a "all_13ths" list: pulling the day of hte week for each
13th day of "month"
4. return count of "all_13ths" 

Code

'''

import datetime

def friday_the_13ths(year):
    all_13ths = [datetime.date(year, month, 13) for month in range(1, 13)]

    count = 0
    for day in all_13ths:
        if day.weekday() == 4:
            count += 1

    return count

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
