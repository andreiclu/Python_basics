"""Find the Primorial
A Primorial is a product of the first n prime numbers (e.g. 2 x 3 x 5 = 30). 2, 3, 5, 7, 11, 13 are prime numbers. If n was 3, you'd multiply 2 x 3 x 5 = 30 or Primorial = 30.

Create a function that returns the Primorial of a number.

Examples
primorial(1) ➞ 2

primorial(2) ➞ 6

primorial(8) ➞ 9699690"""
import numpy


def is_prime(n):
    for i in range(2, n//2+1):
        if (n%i==0):
            return 0
    return 1

def primorial(n):
    lst = []
    i = 2
    while 1:
        if is_prime(i):
            lst.append(i)
            if(len(lst)==n):
                rez = numpy.prod(lst)
                return rez
        i+=1






print(primorial(8))