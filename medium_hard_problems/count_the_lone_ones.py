"""Count the Lone Ones
Create a function which counts how many lone 1s appear in a given number.
Lone means the number doesn't appear twice or more in a row.

Examples
count_lone_ones(101) ➞ 2

count_lone_ones(1191) ➞ 1

count_lone_ones(1111) ➞ 0

count_lone_ones(462) ➞ 0"""



import re

def count_lone_ones(n):
    x = re.split('[^1]', str(n))
    sum = 0
    for i in x:
        if i == '1':
            sum+=1
    return sum

print(count_lone_ones(1191))

print(count_lone_ones(101))