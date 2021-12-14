# Să se insereze într-un șir după fiecare element par dublul său.
x = list(map(int,input("Insert a list of numbers: ").split()))
l = []
for i in x:
    if i % 2 == 0:
        l.append(i)
        l.append(i*i)
print (f"Your new list of numbers are: {l}")

