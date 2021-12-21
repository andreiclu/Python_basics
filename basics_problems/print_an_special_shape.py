# Se citeste un numar natural n cu cel mult 2 cifre.
# Afisati pe ecran o figura formata din caracterul * ca in exemplul de mai jos pentru n=5.

"""
*
**
***
****
*****
     *****
     ****
     ***
     **
     *
"""

x = int(input("Insert a number up to 99: "))
sec_x = x
for i in range(1,x+1):
    print("*"*i)
for n in range(sec_x,0,-1):
    print(' '*(sec_x) + '*'*n)
