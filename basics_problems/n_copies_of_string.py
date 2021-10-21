# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

def string(str, n):
    result= ""
    for i in range(n):
        result = result + str
    return result



x = input("What's your text:")
y = int(input("Number of copies:"))
print(string(x, y))
