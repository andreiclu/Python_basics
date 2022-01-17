a = [1, 2, [3,4], [5,6]]


sum = 0
for i in a:
    if isinstance(i,list):
        for j in i:
            sum += j
    else:
        sum += i

print(sum)

