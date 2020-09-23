import math
import re


def find_d(coefficients):
    a = coefficients[0]
    b = coefficients[1]
    c = coefficients[2]
    d = b**2 - 4 * a * c
    if d < 0:
        print("\nThe discriminant is less than zero, therefore there are no solution")
    elif d == 0:
        print("\nThe discriminant is zero, therefore there is one solution")
        find_x_d0(a, b)
    else:
        print("\nThe discriminant is above zero, therefore there are two solutions")
        find_x(a, b, d)


def find_x(a, b, d):
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("\nThe roots of " + poly + " are:")
    print("x1 = " + str(round(x1)))
    print("x2 = " + str(round(x2)))


def find_x_d0(a, b):
    x = -b / (2 * a)
    print("\nThe root of " + poly + " is:")
    print("x = " + str(round(x)))


def run():
    global poly
    poly = input("please enter a polynomial: ")
    COEFFICIENT_PATTERN = re.compile(r"(?<!x\^)(?<!x\^-)-?\d+")
    coefficients = [int(c) for c in COEFFICIENT_PATTERN.findall(poly)]
    find_d(coefficients)


run()
