# Create a string made of the first, middle and last character
str = input("Give me a string: ")

print("Original string is:", str)

res = str[0]
l = len(str)
mid = int(l / 2)

res = res + str[mid]

res = res + str[l - 1]

print("New string with the first, middle and last char: ", res)
# Create a string made of the middle three characters
str1 = input("Give me a string: ")

print("Original string is:", str1)

mid = int(len(str1)/2)

res = str1[mid-1:mid+2]
print("Your middle three chars are:", res)
# Append new string in the middle of a given string

str = input("Give me a string: ")
mid = input("Give me the string you want to put at the middle of first one: ")

l = int(len(str)/2)
x = str[:l]
x = x + mid
x = x + str[l:]
print("After appending the new string in middle you got: ", x)