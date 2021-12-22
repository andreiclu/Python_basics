"""
Se da un interval [a,b].
Afisati cate dintre numerele din intervalul [a,b] au proprietatea ca atat ele cat si rasturnatul lor sunt patrate perfecte (ex: 144 si 441). Se cere un algoritm eficient din punct de vederea al timpului de executie.
Exemplu: pentru intervalul [100,1000] sunt 10 astfel de numere.
"""

from math import sqrt

a = int(input("Where the interval starts: "))
b = int(input("Where the interval ends: "))
for i in range(a,b+1):
    root = sqrt(i)
    revs = 0
    nr = i
    while(i>0):
        rem = i%10
        revs = revs*10 + rem
        i = i//10
    root_revs = sqrt(revs)
    if int(root+0.5) ** 2 == nr and int(root_revs+0.5) ** 2 == revs:
        print(f"We found these nr to be perfect square with it's reversed too: {(nr,revs)}")

