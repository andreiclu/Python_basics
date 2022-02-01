"""
Write a Python program (recursive and iterative) to calculate the sum of a list of numbers by hand and using Python functions.
"""


def sum_iter(x):
    sum = 0
    for i in x:
        sum = sum + i
    return sum


print(sum_iter([1,2,4,5,6,7,8]))

def sum_rec(x):
    if len(x) == 0:
        return 0
    else:
        return x[0] + sum_rec(x[1:])

print(sum_rec([1,2,4,5,6,7,8]))



def sum_pop(x):
    new = x.pop
    if len(x) == 0:
        return 0
    else:
        return new + x

print(sum_rec([1,2,4,5,6,7,8]))




