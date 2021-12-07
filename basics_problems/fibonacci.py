# Fibonacci of the first 10 nr
n = 0
n1= 1

for i in range(10):
    print(n, end=" ")
    rez = n + n1

    n=n1
    n1=rez