"""
Se citesc două numere naturale a și b (a mai mic decât b) având cel mult 9 cifre fiecare. Afișați câte numere din intervalul [a,b] au exact 3 divizori.
Exemplu:
În intervalul [11,50] numerele care au exact 3 divizori sunt 25 și 49, deci se va afișa 2.

"""
a = int(input("Insert first number, where the interval will star: "))
b = int(input("Insert second number, where the interval will end: "))
def count_of_div(x):
    count = 0
    for i in range(a, b+1):
        if x % i == 0:
            count +=1
    return count
def check_3_fact(a,b):
    c = 0
    for z in range(a, b+1):
        if count_of_div(z) == 3:
            c +=1
            print(f"The number which has exactly 3 divisors are: {z}")
            print(f"Total: {c}")

check_3_fact(a,b)