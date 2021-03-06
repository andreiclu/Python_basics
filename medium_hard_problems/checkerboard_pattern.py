"""
Checkerboard Pattern
Create a function that returns True if the two-dimensional n x n input array has a checker-board pattern.

Examples
is_checkerboard([
  [1, 1],
  [0, 1]
]) ➞ False

is_checkerboard([
  [0, 1],
  [1, 0]
]) ➞ True

is_checkerboard([
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 1, 1]
]) ➞ False

is_checkerboard([
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1]
]) ➞ True
"""

def is_checkerboard(lst):


    for i in range(len(lst)):
        for j in range(1,len(lst)):
            if lst[i][j]==lst[i][j-1]:
                return False

    for j in range(len(lst)):
        for i in range(1,len(lst)):
            if lst[i][j]==lst[i-1][j]:
                return False

    return True


print(is_checkerboard([
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1]
]))


print(is_checkerboard([
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0],
  [1, 0, 1, 1, 1]
]))