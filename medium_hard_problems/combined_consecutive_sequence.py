"""
Write a function that returns True if two arrays, when combined, form a consecutive sequence.
A consecutive sequence is a sequence without any gaps in the integers,
e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.
"""


from typing import List
def consecutive_comb(x: List[int], y: List[int]):
    list_of_all = x+y
    for i in range(min(list_of_all), max(list_of_all)+1):
        if i not in list_of_all:
            return False
    return True

print(consecutive_comb([7, 4, 5, 1], [2, 3, 6]))

