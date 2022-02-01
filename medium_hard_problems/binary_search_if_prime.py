


"""
Create a function that finds a target number in a list of prime numbers. Implement a binary search algorithm in your function. The target number will be from 2 through 97. If the target is prime then return "yes" else return "no".

Examples
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


is_prime(primes, 3) ➞ "yes"

is_prime(primes, 4) ➞ "no"

is_prime(primes, 67) ➞ "yes"

is_prime(primes, 36) ➞ "no"
"""
from sympy import isprime


def is_prime(lst, item):
    begin_index = 0
    end_index = len(lst)-1

    while begin_index <= end_index:
        mid = begin_index + (end_index-begin_index)//2
        mid_val = lst[mid]

        if mid_val == item:
            return "Yes"
        elif item < mid_val:
            end_index = mid - 1
        else:
            begin_index = mid + 1
    return "No"



primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print(is_prime(primes, 3))

print(is_prime(primes, 4))

print(is_prime(primes, 67))

print(is_prime(primes, 36))