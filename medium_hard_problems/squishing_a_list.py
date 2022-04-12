"""
Squishing a List
Write a function that squishes a list from the left or the right.

Examples
squish([1, 2, 3, 4, 5], "left")
➞ [[1, 2, 3, 4, 5], [3, 3, 4, 5], [6, 4, 5], [10, 5], [15]]

squish([1, 2, 3, 4, 5], "right")
➞ [[1, 2, 3, 4, 5], [1, 2, 3, 9], [1, 2, 12], [1, 14], [15]]

squish([1, 0, 2, -3], "left")
➞ [[1, 0, 2, -3], [1, 2, -3], [3, -3], [0]]

squish([1, 0, 2, -3], "right")
➞ [[1, 0, 2, -3], [1, 0, -1], [1, -1], [0]]
Notes
Squishing from the left is to successively sum the first two elements of a list (shortening the list in the process).
Squishing from the right is to successively sum the last two elements of a list.
Include the original list as the first element in either squish.
Return an empty list if the input is an empty list.
"""


def squish(lst, d):
    if not lst: return []
    res = [lst]
    for i in range(len(lst) - 1):
        if d == 'left':
            res.append([sum(res[-1][:2])] + res[-1][2:])
        else:
            res.append(res[-1][:-2] + [sum(res[-1][-2:])])
    return res


print(squish([1, 0, 2, -3], "right"))
