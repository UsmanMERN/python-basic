given_number = 10
sum_even = 0

for i in range(1, given_number + 1):
    if i == 5:
        continue
    print(given_number, " x ", i, " = ", given_number * i)
