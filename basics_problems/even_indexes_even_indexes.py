# Se citește un vector cu n elemente, numere naturale. Să se afișeze elementele cu indici pari în ordinea crescătoare a indicilor,
# iar elementele cu indici impari în ordinea descrescătoare a indicilor.

x = list(map(int,input("Give me a list of numbers: ").split()))

list_of_even_idex = []
list_of_odd_idex = []
for i in x:
    if x.index(i)%2==0:
        list_of_even_idex.append(i)
    else:
        list_of_odd_idex.append(i)


print(f"The list with even idexes is: {list_of_even_idex} and the list with odd ones are: {list_of_odd_idex[::-1]}")


