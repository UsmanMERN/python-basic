import time


def cache(func):
    cache_value = {}
    print(cache_value)

    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]

        result = func(*args)
        cache_value[args] = result
        return result

    return wrapper


@cache
def long_runnig_func(a, b):
    time.sleep(4)
    return a + b


print(long_runnig_func(2, 3))
print(long_runnig_func(2, 8))
print(long_runnig_func(2, 3))
