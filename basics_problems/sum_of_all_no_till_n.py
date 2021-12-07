#Calculate the sum of all numbers from 1 to a given number

x = int(input("Give me an integer: "))
sum = 0
for i in range(x):
    sum = sum + i
print("The sum from 1 to your offered number is: ", sum)


