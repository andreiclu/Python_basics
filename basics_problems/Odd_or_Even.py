#
# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.


x = int(input("Give me a number to check if is odd or even:"))

if x%2==0:
    print('Your number is Even')
else:
    print("Your number is Odd")