# Se dă un vector x cu n elemente numere naturale, ordonate crescător, și un vector y cu m elemente, de asemenea numere naturale. Verificați pentru fiecare element al vectorului y dacă
# apare în x.

x = list(map(int, input("Give me a list of natural numbers: ").split()))

y = list(map(int, input("Give me a second list of natural numbers: ").split()))

x = sorted(x)
new_list = []
for i in x:
    for j in y:
        if i == j:
            new_list.append(i)

if new_list == []:
    print("Sorry, we dind't found anything from y in x")
else:
    print(f" Yes we found something: {new_list}")