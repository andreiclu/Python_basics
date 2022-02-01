
"""
# Se citesc doua numere naturale a si b.
# Afisati toate perechile de numere x si y din intervalul [a,b]
# care au proprietatea ca sunt prime intre ele, dar x si y nu sunt numere prime (exemplu 14 si 25 sunt prime intre ele, dar nici 14 si nici 25 nu sunt numere prime).
# """


from itertools import combinations as comb

from sympy import isprime

a = int(input("Insert where the interval starts: "))
b = int(input("Insert where the interval ends: "))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


x = [i for i in range(a,b+1)]
tuples = []
for i in comb(x,2):
    tuples.append(i)
for val in tuples:
    lstofval = list(val)
    for i in lstofval:
        flag = 0
        if isprime(i) == True:
            flag = 1
            break
        else:
            flag = 0


    if gcd(*val) == 1 and flag == 0:
        print(f"We found the pairs that are prime one for each other but the number's aren't: {val}")

