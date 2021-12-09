x = list(map(int,input("Give me a list of numbers:").split()))

y = list(map(int,input("Give me a list of numbers:").split()))

print(f"Prima multime este: {x}")
print(f"A doua multime este: {y}")

reuninunea = []
intersectia = []

for i in x:
    for j in y:
        if i == j:
            reuninunea.append(i)
        else: intersectia.append(i), intersectia.append(j)

print(f"Reuniunrea celor doua multimi este:\n {reuninunea}\n Iar intersectia celor doua multimi este:")
print(set(intersectia))
