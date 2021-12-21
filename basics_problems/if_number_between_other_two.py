"""
Folosind operatorul conditional, determinati daca o valoare x
apartine intervalului [a,b]. Variabilele a, b si x se citesc de la tastatura,
iar rezultatul va fi afisat sub forma "DA" sau "NU".
"""

a = int(input("Insert the start point: "))
b = int(input("Insert the endpoint: "))
x = int(input("Insert the number to see if is between a and b: "))

for i in range(a,b):
    if i == x:
        print(f"Yes! Found the number {x} between {a} and {b}")
    else:
        print("No! Didn't find nothing")