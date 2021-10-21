# Write a Python program to count a number  in a given list.

x = input("Give my a list of numbers")

y = x.split(",")

z = input("What's your number to count:")

el_count = y.count(z)

print("The count of element in your list is:", el_count)

