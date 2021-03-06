"""
Write a function that returns the greatest common divisor of all list elements. If the greatest common divisor is 1, return 1.

Examples
GCD([10, 20, 40]) ➞ 10

GCD([1, 2, 3, 100]) ➞ 1

GCD([1024, 192, 2048, 512]) ➞ 64
"""
from functools import reduce


def GCD(lst):
    return reduce(gcd, lst)


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

print(GCD([1024, 192, 2048, 512]))

