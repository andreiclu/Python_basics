
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
# from sympy import isprime
# a = int(input("Insert where the interval starts: "))
# b = int(input("Insert where the interval ends"))
#
# for x in range(a,b+1):
#     for y in range(x+1,b+1):
#         while(x!=y):
#             if(x>y):
#                 x = x-y
#             else:
#                 y = y-x
#         prx = isprime(x)
#         pry = isprime(y)
#         if(x==1 and prx==False and pry==False):
#             print((x,y))

"""
Se citeste un numar natural n si apoi n numere naturale. Afisati cate dintre ele au suma cifrelor egala cu numarul de lor de ordine de la citire.
Exemplu: n=6 si numerele 122 101 34 555 23 123
Se va afisa 3 deoarece numerele care respecta regula sunt 101 , 23 si 123.
"""


