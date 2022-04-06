"""
In this challenge, you are given a list of one or more arithmetic operators and a list of numbers. Take each of the operators and mate it with any three separate numbers in the list to create a valid equation. Your answer should contain all possible equations.

Examples
jumbled([["+"], [2, 1, 3]]) ➞ ["1+2=3"]

jumbled([["+", "*"], [36, 28, 71, 4, 12, 7, 11]]) ➞ ["4*7=28", "4+7=11"]

jumbled([["+", "-", "*", "**"], [1, 2, 3, 0]]) ➞ ["1+2=3", "2**0=1", "3**0=1", "3-1=2", "3-2=1"]
# Each equation must contain 3 discrete numbers from the list.
# "1+0=1" or "3-3=0" are not allowed.
"""
from itertools import permutations
def jumbled(lst):
    rez = []
    p = permutations(lst[1],3)

    for i in p:
        for op in lst[0]:
            if op in '+*/&' and i[0]>i[1]:
                continue
            if eval(str(i[0])+op+str(i[1]))== i[2]:
                rez.append('{}{}{}=={}'.format(i[0],op,i[1],i[2]))

    return rez


print(jumbled([["+", "*"], [36, 28, 71, 4, 12, 7, 11]]))

print(jumbled([["+"], [2, 1, 3]]))