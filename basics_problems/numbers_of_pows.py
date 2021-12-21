"""
Se citesc doua numere naturale n si p.
Afisati in ordine crescatoare toate puterile lui n care sunt mai mici sau egale cu p.
Exemplu:
Pentru n=4 si p=120 se vor afisa 1 4 16 64
"""

n = int(input("Insert a number: "))
p = int(input("Insert another number: "))

power = 1
print(power)
for i in range(n,p):
    if n**power <=p:
        print(n**power)
        power += 1