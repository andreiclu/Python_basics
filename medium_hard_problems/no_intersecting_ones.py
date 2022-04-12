"""
No Intersecting Ones
A no-intersecting ones matrix is one where no two ones exist on the same row or column.

To illustrate:

[
  [1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0]
]
The list below is not a non-intersecting ones matrix:

[
  [1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 0, 0]
]

// Column 2 has two 1s.
Write a function that returns True if a 2D matrix is a no-intersecting ones matrix and False otherwise.

Examples
no_intersecting_nes([
  [0, 1],
  [1, 0]
]) ➞ True

no_intersecting_ones([
  [1, 1],
  [0, 0]
]) ➞ False

no_intersecting_ones([
  [0, 0, 0, 1],
  [1, 0, 0, 0],
  [0, 1, 0, 0]
]) ➞ True
"""


def no_intersecting_ones(lst):
    for i in range(len(lst[0])):
        out = []
        for j in range(len(lst)):
            if lst[j].count(1) > 1:
                return False
            out.append(lst[j][i])
        if out.count(1) > 1:
            return False
    return True


print(no_intersecting_ones([
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0]
]))

print(no_intersecting_ones([
  [1, 1],
  [0, 0]
]))