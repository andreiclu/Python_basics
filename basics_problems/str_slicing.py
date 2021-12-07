 # Write a program that operates on a provided string, that always has length of at least 10
# characters.
# a. If the string length is even, retrieve a substring that is exactly 4 characters long and is
# exactly in the middle of the original string.
# b. If the string length is odd, retrieve a substring that is exactly 5 characters long and is
# exactly in the middle of the original string.


x = input("Give me a string: ")
mid = len(x)//2
if len(x)%2 == 0:
    print(x[mid-2:mid+2])
else:
    print(x[mid-2:mid+3])
