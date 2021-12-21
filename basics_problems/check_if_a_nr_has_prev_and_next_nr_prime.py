"""

Se citesc doua numere naturale a si b.
Calculati si afisati cate numere din intervalul [a,b] au proprietatea ca sunt incadrate de doua numere prime. Un astfel de numar este 12 (11 si 13 sunt prime).
Exemplu:
In intervalul [10,30] sunt 3 astfel de numere (12, 18 si 30)
"""

from sympy import isprime

a = int(input("Insert first number, where the interval will star: "))
b = int(input("Insert second number, where the interval will end: "))

nr = 0

for i in range(a,b+1):
    x = i-1
    y = i+1
    pr_x = 1
    if isprime(x) and isprime(y):
        print(i)

