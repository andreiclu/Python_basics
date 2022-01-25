"""Given a word, create a function which returns whether or not it's possible to create a palindrome by rearranging the letters in the word.

Examples
is_palindrome_possible("rearcac") ➞ True
# You can make "racecar"

is_palindrome_possible("suhbeusheff") ➞ True
# You can make "sfuehbheufs" (not a real word but still a palindrome)

is_palindrome_possible("palindrome") ➞ False
# It's impossible"""


import math
import random

def is_palindrome_possible(txt):
    lst = []

    for i in txt:
        if i not in lst: lst.append(i)
        else: continue

    fc = 0

    for val in lst:
        if txt.count(val)%2 == 0: continue
        else: fc +=1
    if fc >1: return False
    else: return True



print(is_palindrome_possible("rearcac"))

print(is_palindrome_possible("suhbeusheff"))

print(is_palindrome_possible("palindrome"))