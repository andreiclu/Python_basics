"""
Se citesc numere naturale p�n� c�nd se introduce num�rul 0.
Afisati suma obtinut� prin adunarea primei si a ultimei cifre din fiecare numar citit. Numerele cu mai putin de 2 cifre nu se iau in considerare.
Exemplu: dac� se introduc numerele 3455 66 7 8 23 11221 0 atunci se va afisa 27 (3+5+6+6+2+3+1+1).
"""

x = list(map(int,input("Insert a list of numbers for making the sum of first and last digit of every number: ").split()))

lst_of_first_and_last_dig = []
for i in x:
    if i>=10:
        f_d = int(str(i)[0])
        l_d = int(str(i)[-1])
        lst_of_first_and_last_dig.append(f_d)
        lst_of_first_and_last_dig.append(l_d)
rez = sum(lst_of_first_and_last_dig)
print(rez)
