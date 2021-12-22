"""
Se citesc un numar natural n si o cifra c.
Eliminati toate aparitiile cifrei c din numarul n si afisati numarul astfel obtinut.
Exemplu: n= 2345324 , c=2 rezulta numarul 34534
"""
n =input("Insert a big natural number and let's remove a digit: ")
d =input("The digit we want to delete from the number: ")

for i in n:
    if i == d:
        rez = n.replace(i,"")
print(rez)

