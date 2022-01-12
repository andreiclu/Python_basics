"""
A number can eat the number to the right of it if it's smaller than itself. After eating that number, it becomes the sum of itself and that number.
Your job is to create a function that returns the final list after the leftmost element has finished "eating".
"""



from typing import List

def nom_nom(x : List[int]):
    for i in range(2):
        if x[0] > x[1]:
            x[1] = x[0] + x[1]
            del x[0]
    return x

print(nom_nom([8, 5, 9]))

print(nom_nom([2, 1, 3]))