"""
Goldbach's Conjecture is amongst the oldest and well-known unsolved mathematical problems. In correspondence with Leonhard Euler in 1742, German mathematician Christian Goldbach made a conjecture, which states:

"Every even whole number greater than 2 is the sum of two prime numbers."

Even though it's been thoroughly tested and analyzed and seems to be true, it hasn't been proved yet (thus, remaining a conjecture.)

Create a function that takes a number and returns an array as per the following rules:

If the given number is odd and greater than two, return an empty array.
If the given number is even and greater than two, return an array of two prime numbers whose sum is the given input.
Both prime numbers must be the farthest (with the greatest difference).
Examples
goldbach_conjecture(1) ➞ []
# The given number is not greater than 2.

goldbach_conjecture(7) ➞ []
# The given number is not an even number.

goldbach_conjecture(14) ➞ [3, 11]
Notes
Return list in sequence: [smaller, bigger]
"""
from sympy import isprime


def goldbach_conjecture(n):

    for i in range(2,n):
        if isprime(i) and isprime(n-i):
            return [i,n-i]
    return []
#primes = all(n%i for i in range(2, n//2+1)
print((goldbach_conjecture(3444)))
