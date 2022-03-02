"""
List with Zero Sum
Given an integer n, return any list containing n unique integers such that they add up to 0.

Examples
list_with_zero_sum(5) ➞ [-7, -1, 1, 3, 4] or [-5, -1, 1, 2, 3] or [-3, -1, 2, -2, 4]

list_with_zero_sum(3) ➞ [-1, 0, 1]

list_with_zero_sum(1) ➞ [0]
"""


def list_with_zero_sum(n):
    rez = []
    if n%2:
        rez.append(0)
    for i in range(1,n//2+1):
        rez +=[i,-i]

    return rez


print(list_with_zero_sum(11))










