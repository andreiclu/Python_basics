#Fibonacci pentru primele 10:


n = 0
n1= 1

for i in range(10):# 1000 ar fi prea mult
    print(n, end=" ")
    rez = n + n1

    n=n1
    n1=rez

# A better version:


# Program to display the Fibonacci sequence up to how many numbers we want

# terms = int(input("How many terms? "))
#
# # primele doua numere ce trebuie declarate
# n1, n2 = 0, 1
# count = 0
#
# # check if the number of terms is valid
# if terms <= 1:
#    print("Please enter a positive integer, bigger than 1")
# else:
#    print("Fibonacci sequence:")
#    while count < terms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1
#
