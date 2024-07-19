import math


def circle_stats(raduis):
    area = math.pi * raduis**2
    circumference = 2 * math.pi * raduis
    return area, circumference


a, c = circle_stats(12)

print("Area", a.__round__(2))
print("circumference", c.__round__(3))
