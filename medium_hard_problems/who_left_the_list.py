"""
You are given two lists.
The elements in lst1 threw a party and started to mix around.
However, one of the elements got lost!
Your task is to return the element which was lost.
"""


def missing_elem(x,y):
    for el in x:
        if el not in y:
            return el
print(missing_elem(["Jane", "is", "pretty", "ugly"], ["Jane", "is", "pretty"]))
print(missing_elem(["different", "types", "5", 5, [5], (5,)], ["5", "different", [5], "types", 5]))