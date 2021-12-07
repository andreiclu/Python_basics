# Să se șteargă dintr-un șir elementul aflat pe o poziție dată.

x = list(map(int, input("Give me a list of numbers: ").split()))

y = int(input("Give me the postion from where you want to delete a number: "))

del x[y-1]
print(x)
