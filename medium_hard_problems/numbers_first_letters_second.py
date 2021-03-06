"""
Write a function that sorts list while keeping the list structure. Numbers should be first then letters both in ascending order.

Examples
num_then_char([
  [1, 2, 4, 3, "a", "b"],
  [6, "c", 5], [7, "d"],
  ["f", "e", 8]
]) ➞ [
  [1, 2, 3, 4, 5, 6],
  [7, 8, "a"],
  ["b", "c"], ["d", "e", "f"]
]

num_then_char([
  [1, 2, 4.4, "f", "a", "b"],
  [0], [0.5, "d","X",3,"s"],
  ["f", "e", 8],
  ["p","Y","Z"],
  [12,18]
]) ➞ [
  [0, 0.5, 1, 2, 3, 4.4],
  [8],
  [12, 18, "X", "Y", "Z"],
  ["a", "b", "d"],
  ["e", "f", "f"],
  ["p", "s"]
]
"""

def num_then_char(lst):
    nums, letters = [], []
    for L in lst:
        for a in L:
            if type(a) == str:
                letters.append(a)
            else:
                nums.append(a)
    nums.sort()
    letters.sort()
    L = nums + letters
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = L.pop(0)
    return lst

print(num_then_char([
  [1, 2, 4.4, "f", "a", "b"],
  [0], [0.5, "d","X",3,"s"],
  ["f", "e", 8],
  ["p","Y","Z"],
  [12,18]
]))
