"""
Se citesc de la tastatura doua numere naturale a si b cu exact doua cifre fiecare.
Scrieti un program care afiseaza numarul total de cifre pare din cele doua numere daca ele au aceeasi paritate, iar daca au paritati diferite atunci afiseaza numarul total de cifre impare din cele doua numere.
Exemple: Daca a = 78 si b = 18 se va afisa 2 (8 si 8 sunt cifrele pare, adica 2)
Daca a = 36 si b= 55 se va afisa 3 (sunt 3 cifre impare, si anume 3, 5, 5)
Rezolvare

"""



x = int(input("Insert a number of two digits: "))
y = int(input('Insert another number of two digits: '))

count = 0
if x % 2 ==0 and y % 2 == 0:
    a1 = x//10
    a2 = x%10
    b1 = y//10
    b2 = y&10
    if a1%2 == 0:
        count +=1
    if a2%2 == 0:
        count +=1
    if b1%2 == 0:
        count +=1
    if b2%2 == 0:
        count +=1
    print(f" The digits for first number are: {a1} and {a2} and for the second number are {b1} and {b2} and there is {count} even numbers in {x} and {y}")
else:
    a1 = x // 10
    a2 = x % 10
    b1 = y // 10
    b2 = y & 10
    if a1 % 2 != 0:
        count += 1
    if a2 % 2 != 0:
        count += 1
    if b1 % 2 != 0:
        count += 1
    if b2 % 2 != 0:
        count += 1
    print(f" The digits for first number are: {a1} and {a2} and for the second number are {b1} and {b2} and there is {count} odd numbers in {x} and {y}")
