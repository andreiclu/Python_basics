"""
Lonely Numbers
Given a number, insert duplicate digits on both sides of all digits which appear in a group of 1.

Worked Example
numbers_need_friends_too(22733) ➞ 2277733

# The number can be split into groups 22, 7, and 33.
# 7 appears on its own.
# Put 7s on both sides to create 777.
# Put the numbers together and return the result.
Examples
numbers_need_friends_too(123) ➞ 111222333

numbers_need_friends_too(56657) ➞ 55566555777

numbers_need_friends_too(33) ➞ 33
"""


def numbers_need_friends_too(n):
    st = str(n)
    groups = []
    current = ''

    for i in st:
        if i in current or current =='':
            current+=i
        else:
            groups.append(current)
            current = i
    if current!='':
        groups.append(current)

    for i in range(len(groups)):
        if len(groups[i])==1:
            groups[i] = groups[i].replace(groups[i][0], groups[i][0]*3,1)
    return int(''.join(groups))


print(numbers_need_friends_too(56657))

print(numbers_need_friends_too(123))