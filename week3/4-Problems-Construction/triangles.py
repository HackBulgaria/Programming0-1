from math import sqrt


# Прилагаме неравенството на триъгълника директно
def is_triangle(a, b, c):
    return a + b > c and a + c > b and c + b > a


# Прилагаме директно Хероновата формула
# p е полупериметъра
def area(a, b, c):
    p = (a + b + c) / 2

    return sqrt(p * (p - a) * (p - b) * (p - c))


# Правим директната приверка, при условието, че c е хипотенузата
def is_pythagorean(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


# Това е същата задача, като да намерим максималното число в списък,
# Само че трябва да свършим работата за това да превърнем триъгълник в неговото лице (число)
def max_area(triangles):
    current_max = triangles[0]

    a = current_max[0]
    b = current_max[1]
    c = current_max[2]

    current_max_area = area(a, b, c)

    for triangle in triangles:
        a = triangle[0]
        b = triangle[1]
        c = triangle[2]

        current_area = area(a, b, c)

        if current_area > current_max_area:
            current_max = triangle
            current_max_area = current_area

    return current_max
