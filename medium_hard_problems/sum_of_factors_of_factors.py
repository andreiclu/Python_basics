"""Sum of Factors of Factors
Create a function that takes a number and returns the sum of factors of factors of the given number.

Examples
sum_ff(69) ➞ 3, 23 ➞ 0
# Both 3 and 23 are prime numbers and have no factors
# other than 1 and themselves so the result is 0.

sum_ff(12) ➞ 2, 3, 4, 6 ➞ (0) + (0) + (2) + (2+3) ➞ 7

sum_ff(420) ➞ 2,4, 6, 10, 12 ... ➞ (2) + (2+3) + (2+5) + (2+3+4+6) ... ➞ 1175

sum_ff(619) ➞ ___ ➞ 0
# 619 doesn't have any factors (other than 1 and 619)."""

def fact(x):
    lst = []
    for i in range(2,x//2+1):
        if x%i == 0:
            lst.append(i)
    return lst

def sum_ff(n):
    s = 0
    for i in fact(n):
        x = fact(i)
        if len(x) > 0:
            s+=sum(x)
    return s




print(sum_ff(619))

print(sum_ff(420))

print(sum_ff(12))