"""
Create a function that takes two integers, num and n, and returns an integer which is divisible by n and is the closest to num. If there are two numbers equidistant from num and divisible by n, select the larger one.

Examples
round_number(33, 25) ➞ 25

round_number(46, 7) ➞ 49

round_number(133, 14) ➞ 140
Notes
n will always be a positive number.
"""

def round_number(num,n):
    down = num%n
    up = -num%n

    if down<up:
        return num-down
    else:
        return num + up


print((round_number(12121212, 144)))