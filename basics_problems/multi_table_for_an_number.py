# Write a program to print multiplication table of a given number


x = int(input("Give me an integer for multiplication purposes: "))
m = 2
for i in range(1, 11):
    p = m * i
    print("The multiplication table for your number is: ", p)
