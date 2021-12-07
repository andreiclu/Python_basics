#Factorial of a given number

x = int(input(" Give me an nr: "))
fact = 1
for i in range(1,x+1):
    fact = fact * i
print("Factorial of the given number is: ", fact)