def sum_all(*args):
    for i in args:
        print(i * 2)
    return sum(args)


print(sum_all(2, 3, 4, 2, 3))
# print(sum_all(2, 3, 9, 8, 3))
