#Se citește numărul natural n. Să se determine exponentul maxim e cu proprietatea că 2e ≤ n.

x = int(input("Give me the number: "))

rez = 0
for i in range(0,x):
    if 2**i <= x:
        rez = rez + 1
print(rez)
