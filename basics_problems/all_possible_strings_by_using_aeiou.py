# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
#
# import random as rd
#
# list = ['a', 'e', 'i', 'o', 'u']
# rd.shuffle(list)
# print(''.join(list))

from itertools import permutations

char = ['a', 'e', 'i', 'o', 'u']

allstr = permutations(char)

for string in allstr:
    print(''.join(string))

