import math

def circle_stats(radius):
    area = (math.pi * radius ** 2).__round__(2)
    circumference = round(2 * math.pi * radius , 2)
    calc = f"Area: {area}, Circumference: {circumference}"
    return calc

print(circle_stats(5))
print(circle_stats(10))