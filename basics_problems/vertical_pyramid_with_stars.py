

x = int(input("Give me an number from 1 to 10 to initialize a star pattern:"))

for i in range(x):
    for j in range(0,i+1):
        print('*', end=" ")
    print("\r")
for i in range(x,0,-1):
    for j in range(0,i-1):
        print('*', end=" ")
    print('\r')
