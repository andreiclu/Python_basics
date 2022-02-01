# Să se scrie un program care citește un șir de n
# numere naturale şi determină valoarea maximă din șir și de câte ori apare.

l = list(map(int, input('Enter numbers: ').split()))

count = 0
for i in l:
    if i == max(l):
        count +=1
print(max(l), count)
