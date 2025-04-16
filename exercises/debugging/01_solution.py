def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    # decrease(counter)
    counter = decrease(counter)


print('LAUNCH!')