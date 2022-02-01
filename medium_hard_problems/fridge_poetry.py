"""
Fridge Poetry
Write a function that returns True if it's possible to build a phrase txt1 using only the characters from another phrase txt2.

Examples
can_build("got 2 go", "gogogo 2 today") ➞ True

can_build("sit on top", "its a moo point") ➞ True

can_build("long high add or", "highway road go long") ➞ False

can_build("fill tuck mid", "truck falls dim") ➞ False
"""


def can_build(txt1, txt2):
    txt2 = list(txt2)
    for ch in txt1:
        if ch != ' ':
            if ch in txt2:
                txt2.remove(ch)
            else:
                return False
    return True


print(can_build("fill tuck mid", "truck falls dim"))

print(can_build("got 2 go", "gogogo 2 today"))