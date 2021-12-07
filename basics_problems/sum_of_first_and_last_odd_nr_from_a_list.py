

x = list(map(int,input("Give me a list of numbers: ").split()))
new_l = []
for i in x:
    if i%2 != 0:
        new_l.append(i)
sum = new_l[0] + new_l[-1]

print(sum)

