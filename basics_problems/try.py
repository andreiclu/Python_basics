
#
#
# iter = PrimeIterator(20)
# for elem in iter:
#     print(elem)

#
# def sq_numbers(n):
#     for i in range(1,n+1):
#         yield i*i
#
#
# a = sq_numbers(11)
#
# for i in a:
#     print(i)
#
#
# import re
# x = input("Insert a text:")
#
# dict = {
#     "COLEGIUL": "Co.",
#     "LICEUL": "Li.",
#     "NATIONAL": "Nat.",
#     "TEORETIC": "Tr."
# }
#
# # my_set = ('COLEGIUL', 'LICEUL', 'NATIONAL', 'TEORETIC')
#
#
# for i in x:
#     for key, value in dict.items():
#         if key == i:
#             new_str = (re.sub(key, value, new_str))
#             print(new_str)

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
    flag = 0
for val in tuples:
    lstofval = list(val)
    if isprime(all(lstofval)):
        flag = 1
    else:
        flag = 0

    if gcd(*val) == 1 and flag==1:
        print(f"We found the pairs that are prime one for each other but they aren't: {val}")













import re
from typing import List

"""
Se citeste un numar natural n si apoi n numere naturale. Afisati cate dintre ele au suma cifrelor egala cu numarul de lor de ordine de la citire.
Exemplu: n=6 si numerele 122 101 34 555 23 123
Se va afisa 3 deoarece numerele care respecta regula sunt 101 , 23 si 123.
# """
#
# from timeit import timeit
#
# code = '''
# from time import sleep
# def method():
#     sleep(1)
#
# method()
#     '''
#
# print(timeit(code, number=2))

# import re
# sum = 0
# pattern = 'back'
# if re.match(pattern,'backup.txt'):
#     sum+=1
# if re.match(pattern,'text.back'):
#     sum+=2
# if re.match(pattern, 'backup.txt'):
#     sum+=4
# if re.search(pattern, 'text.back'):
#     sum+=8
# print(sum)
#
# param = (i*i for i in range(5))
# print(type(param))
# #
