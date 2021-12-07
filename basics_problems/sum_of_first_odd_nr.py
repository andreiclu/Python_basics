#
#Se dă numărul natural nenul n. Să se determine produsul primelor n numere impare.
x = int(input("Give me the number you want to stop: "))

def sum_of_odd_nr():
    sum = 0
    for i in range (0, x+1):
        if i % 2 != 0:
            sum = sum + i
    return sum

print(sum_of_odd_nr())




