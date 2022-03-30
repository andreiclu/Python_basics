"""
Growing and Shrinking Potions
There are two types of potions:

Growing potion: "A"
Shrinking potion: "B"
If "A" immediately follows a digit, add 1 to the digit.
If "B" immediately follows a digit, subtract 1 from the digit.
Create a function that returns a string according to these rules, removing the potions once they've been consumed.

Examples
after_potion("3A78B51") ➞ "47751"
# 3 grows to 4, 8 shrinks to 7

after_potion("9999B") ➞ "9998"

after_potion("9A123") ➞ "10123"

after_potion("567") ➞ "567"
Notes
Digits that do not have a potion on their immediate right should be left alone.
A digit will always either be followed by zero or exactly 1 potion.
"""


def after_potion(txt):
    lst = list(txt)
    for i in range(1, len(lst)):
        if lst[i] == 'A':
            lst[i - 1] = int(txt[i - 1]) + 1
        if lst[i] == 'B':
            lst[i - 1] = int(txt[i - 1]) - 1

    return ''.join([str(i) for i in lst if i not in ['A','B']])


print(after_potion("9A123"))

print(after_potion("9999B"))