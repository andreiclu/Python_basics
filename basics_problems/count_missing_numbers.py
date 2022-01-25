"""
Count Missing Numbers
Create a function that takes a list of "mostly" numbers, counts the
amount of missing numbers and returns their sum. Watch out for strings!

Examples
count_missing_nums(["1", "3", "5", "7", "9"]) ➞ 4
# 1+1+1+1

count_missing_nums(["7", "3", "1", "9", "5"]) ➞ 4

count_missing_nums(["1", "5", "B", "9", "z"]) ➞ 6
"""


def count_missing_nums(a):
    b = []
    for i in a:
        if i.isdigit():
            b.append(i)

    for i in range(len(b)):
        b[i] = int(b[i])
    res = 9

    for j in range(1,max(b)+1):
        if j in b:
            res = res - 1
    return res


print(count_missing_nums(["7", "3", "1", "9", "5"]))

print(count_missing_nums(["7", "3", "1", "9", "5"]))

print(count_missing_nums(["1", "5", "B", "9", "z"]))

