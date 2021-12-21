"""
Folosind operatorul conditional, calculati de cate sticle de cate x litri fiecare este nevoie pentru a umple un vas de y litri.
Exemplu:
daca x=4 si y=20 , atunci e nevoie de 5 sticle
daca x=4 si y=23 , atunci e nevoie de 6 sticle
"""
from math import ceil
x = int(input("Bottle with how many liters: "))
y = int(input("The bowl we have to full it in is the size of: "))

number_of_b = y/x

print(f"We're gonna need {ceil(number_of_b)} bottels to fill the bowl")

