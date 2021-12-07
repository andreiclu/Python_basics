# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def dif_or_not(data):
    if(len(data)) == len(set(data)):
        return True
    else:
        return False

x= (input("Give me some numbers to see if they're diffrent: "))

print(dif_or_not(x))
