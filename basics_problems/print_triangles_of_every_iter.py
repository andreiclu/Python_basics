"""
Se citeste un numar natural n. Sa se afiseze n triunghiuri ca in exemplu:
pentru n=3 se vor afisa:
1
2
2 2
3
3 3
3 3 3"
"""

n = int(input("Insert a numbeber and let's create triangles with everyone till the last: "))

for m in range(1,n+1):
    for i in range(1,m+1):
        for j in range(1,i+1):
            print(m, end=' ')
        print("\r")

