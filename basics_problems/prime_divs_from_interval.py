"""
Se citesc doua numere naturale a si b (a mai mic decat b).
Afisati numerele din intervalul [a,b] care au proprietatea ca au numar maxim de divizori primi.
Exemplu: a=30, b=45 => 30, 42 (au cate 3 divizori primi, iar restul numerelor au mai putini)
"""

a = int(input("Insert first number,bigger than 1, where the interval will start: "))
b = int(input("Insert second number, where the interval will end: "))
from sympy import isprime

def count_of_div_and_prime(x):
    count = 0
    for i in range(a, b+1):
        if x % i == 0 and isprime(i):
            count +=1
    return count
def check_3_fact(a,b):
    c = 0
    for z in range(a, b+1):
        if count_of_div_and_prime(z) == 3:
            c +=1
            print(f"The number which has exactly 3 prime divisors are: {z}")
            print(f"Total: {c}")


check_3_fact(a,b)
