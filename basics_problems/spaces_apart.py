"""
Create a function that takes an lst and returns the sum of the numbers between two "1"s.

Examples
space_apart([1, 0, 1, "1", 4, 3, 2, 3, 2, "1"]) ➞ 14

space_apart(["1", 9, 20, 38, "1"]) ➞ 67

space_apart([3, 2, 9, "1", 0, 0, -1, "1"]) ➞ "invalid"
Notes
Return "invalid" if:
A negative number exists inside lst.
The number of "1"s does not equal 2.
Ignore any other string inside lst.
Note that "1" is not 1.
"""

def space_apart(lst):
    count = spaces = 0
    for x in lst:
        if x == "1":
            count +=1
        elif count == 1 and type(x) == int and x>0:
            spaces += x
        elif count == 1 and type(x) == int and x < 0:
            break
    return spaces if count == 2 else "invalid"


print(space_apart([1, 0, 1, "1", 4, 3, 2, 3, 2, "1"]))