def debug(func):
    def wrapper(*args, **kwargs):
        return func(*args)

    return wrapper


def hello():
    print("Hello")


def greet(name, greeting="Hello"):
    print(f"{greeting} {name}")


greet("Muhammad Usman", "Good Evening")
# print(greet("Muhammad Usman", "Asslam o Alaikum"))
