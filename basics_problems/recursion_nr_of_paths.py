"""
Write a function that takes two inputs n and m and outputs the number of unique paths
from the top left corner to bottom right corner of a n X m grid.
Constraints: you can only move down or right 1 unit ar time
"""

def grid_paths(n,m):
    if n == 1 or m == 1:
        return 1
    else:
        return grid_paths(n, m-1) + grid_paths(n-1,m)


print(grid_paths(4,5))


