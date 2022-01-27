# Write a Python program to get all possible two digit letter combinations from a digit (1 to 9) string.
#
# string_maps = {
# "1": "abc",
# "2": "def",
# "3": "ghi",
# "4": "jkl",
# "5": "mno",
# "6": "pqrs",
# "7": "tuv",
# "8": "wxy",
# "9": "z"
# }



# def letter_combinations(digits):
#     if digits == "":
#         return []
#     string_maps = {
#         "1": "abc",
#         "2": "def",
#         "3": "ghi",
#         "4": "jkl",
#         "5": "mno",
#         "6": "pqrs",
#         "7": "tuv",
#         "8": "wxy",
#         "9": "z"
#     }
#     result = [""]
#     for num in digits:
#         temp = []
#         for an in result:
#             for char in string_maps[num]:
#                 temp.append(an + char)
#         result = temp
#     return result
#
# digit_string = "47"
# print(letter_combinations(digit_string))
# digit_string = "29"
# print(letter_combinations(digit_string))
#
#


# Write a Python program to compute the digit number of sum of two given integers.
#
# Input:
# Each test case consists of two non-negative integers x and y which are separated by a space in a line.
# 0 ≤ x, y ≤ 1,000,000


# print("Input two integers(a b): ")
# a,b = map(int,input().split(" "))
# print("Number of digit of a and b.:")
# print(len(str(a+b)))


#Write a Python program to print the number of prime numbers which are less than or equal to a given integer



x = input("Give me some strings: ")


s = x.strip(" ","")
print(s)

