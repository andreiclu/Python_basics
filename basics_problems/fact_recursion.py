"""
Să se scrie o funcție C++ recursivă care returnează factorialul unui număr dat ca parametru.
"""

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
#
# print(fact(5))
#

# Using memoization for saving memory:

fac_mem = {}
def fact(n):
    if n < 2: return 1
    if n not in fac_mem:
        fac_mem[n] = n * fact(n-1)
    return fac_mem[n]

print(fact(5))

#or

# import functools
#
# @functools.cache
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
#
# print(fact(5))

