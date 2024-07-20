# username="Usman"

# def func():
#     # username="Muhammad Usman"
#     print(username)

# func()
# print(username)


# x= 99

# def fun2(y):
#     z=x+y
#     return z

# result= fun2(58)

# print(result)

# x=32

# def fun3():
#     global x
#     x=88
#     print(x)


# fun3()
# print(x)

# x=99

# def f1():
#     x=72
#     def f2():
#         print(x)
#     return f2

# my_result=f1()

# my_result()

def learning(num):
    def actual(x):
        return x**num
    return actual

f = learning(2)
g=learning(3)