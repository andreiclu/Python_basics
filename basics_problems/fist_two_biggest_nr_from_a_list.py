# Să se scrie un program care citește un șir de n numere naturale şi
# determină cele mai mari două numere din şir.

l = list(map(int, input("Give me the list of numbers to see the biggest two: ").split()))

a = max(l)
l.remove(a)
b = max(l)

print (f'First biggest number in the list is: {a} and second one is: {b}')


