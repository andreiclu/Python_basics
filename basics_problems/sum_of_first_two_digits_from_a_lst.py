"""
Se citesc numere naturale p�n� c�nd se introduce num�rul 0.
Afisati suma obtinut� prin adunarea primei si a ultimei cifre din fiecare numar citit.
Numerele cu mai putin de 2 cifre nu se iau in considerare.
Exemplu: dac� se introduc numerele 3455 66 7 8 23 11221 0 atunci se va afisa 27 (3+5+6+6+2+3+1+1).
"""

x = list(map(int,input("Insert a list of numbers: ").split()))

lst_of_the_two_dig = []
for i in x:
    if i>=10:
        v = int(str(i)[:2])
        lst_of_the_two_dig.append(v)
rez = sum(lst_of_the_two_dig)
print(rez)
