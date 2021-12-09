# Se dau două şiruri, cu n, respectiv m, elemente, numere naturale. Primul şir este ordonat crescător, iar al doilea element este ordonat descrescător.
# Să se afişeze, în ordine crescătoare, valorile pare din cele două şiruri.




x = sorted(list(map(int,input("Give me a list of numbers:").split())))

y = sorted(list(map(int,input("Give me a list of numbers:").split())), reverse=True)

list_of_numbers= []

for i in x:
    if i%2 == 0:
        list_of_numbers.append(i)
for j in x:
    if j%2 == 0:
        list_of_numbers.append(j)

print(sorted(list_of_numbers))
