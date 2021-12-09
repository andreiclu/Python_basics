# Se dau n numere naturale nenule.
# Ordonați descrescător cele n numere după numărul lor de divizori.

x = list(map(int, input("Give me a list of numbers and let's order the numbers by the biggest divisors : ").split()))
dict = {}
for i in x:
    count = 0
    for z in range(1, i+1):
        if i % z == 0:
            count +=1
    dict[f"Number: {i}"] = [f"Has {count} divisors"]

x = sorted(dict.items(), key=lambda item: item[1], reverse=True)

print(x)


