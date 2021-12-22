"""
Se citeste un numar n si un numar q, q din intervalul [2,9].
Verificati daca n este corect scris in baza q.
Exemple:
pentru n=1372, q=9 raspunsul este da
pentru n=1237, q=7 raspunsul este nu
"""

n = input("Give me a number: ")
q = int(input("Let's check if the number is in your chosen base:"))

lst_of_n = list(n)
for i in lst_of_n:
    i = int(i)
    if i <q:
        fl = 1
    else:
        fl =0
if fl ==1:
    print(f'Yes the number {n} si in {q} base')
else:
    print(f"No, sorry, the number {n} is not in {q} base")

