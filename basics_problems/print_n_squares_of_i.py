"""Se citeste un num�r natural n. Sa se afiseze n p�trate ca in exemplu:
pentru n=3 se vor afisa:
1
2 2
2 2
3 3 3
3 3 3
3 3 3"""

x = int(input("Insert a number and let's create: "))


for i in range(1,x+1):
    for j in range(1,i+1):
        for z in range(1,i+1):
            print(i, end=' ')
        print("\r")
