"""
Factorial of Factorials
Create a function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:

Examples
fact_of_fact(4) ➞ 288
# 4! * 3! * 2! * 1! = 288

fact_of_fact(5) ➞ 34560

fact_of_fact(6) ➞ 24883200
"""


def fact(n):
    return 1 if n<2 else n * fact(n-1)

def fact_of_fact(x):
    return 1 if x<2 else fact(x) * fact_of_fact(x-1)


print(fact_of_fact(5))

print(fact_of_fact(6))
