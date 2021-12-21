"""
Adrian este trimis de mama sa la cumparaturi si are de platit o suma de S lei.
El are in buzunar bancnote cu valorile a, b si c.
Afisati cate bancnote de fiecare fel foloseste astfel incat sa dea vanzatorului cat mai putine bancnote pentru a plati
integral suma S.
Se presupune ca Adrian are suficiente bancnote de fiecare fel.
Datele de intrare asigura ca suma poate fi platita.
Rezultatele se vor afisa ca in exemple, adica nu se vor afisa tipurile de bancnote care nu sunt folosite.
Exemple:
S=75, a=50, b=30, c=5 => se va afisa 1*50 5*5 (va plati 1 de 50 si 5 de 5)
S=170, a =100, b=20, c=10 => se va afisa 1*100 3*20 1*10 (va plati 1 de 100, 3 de 20 si 1 de 10)
"""





a = int(input("Give me the one bill: "))
b = int(input("Give me the one bill: "))
c = int(input("Give me the one bill: "))
S = int(input("Insert the sum to pay: "))

x=S//a
S=S%a
y=S//b
S=S%b
z=S//c
if(x!=0):
    print(f"{x}*{a}")
if(y!=0):
    print(f"{y}*{b}")
if(z!=0):
    print(f"{z}*{c}")
