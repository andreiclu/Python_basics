"""Matryoshka dolls are traditionally wooden dolls that can be nested by fitting smaller dolls into larger ones.
Suppose lists can be nested similarly, placing smaller lists into larger ones, in the following sense:

List A can be nested inside List B if:

min(list A) > min(list B)
max(list A) < max(list B)
For example, if A = [2, 3, 9, 5] and B = [10, 2, 1], then A can be nested inside B, since:

min(A) = 2 > 1 = min(B) and
max(A) = 9 < 10 = max(B)
Create a function that returns True if every single sub-list inside a list can be nested Matroyshka style, and False otherwise.

Examples
matryoshka([[2, 2, 7], [3, 4, 5, 6], [4, 5]]) ➞ True
# [4, 5] nested inside [3, 4, 5, 6], [3, 4, 5, 6] nested inside [2, 2, 7], etc.
# Dolls nested from largest to smallest.

matryoshka([[4, 5], [6, 3], [7, 6, 5, 4, 3, 2], [8, 1]]) ➞ True
# Dolls nested from smallest to largest.

matryoshka([[7, 1], [7, 6, 5, 4, 3, 2], [6, 3], [4, 5]]) ➞ False
# [7, 1] and [7, 6, 5, 4, 3, 2] share the same max.
# Second doll cannot be nested properly inside first doll.

matryoshka([[1, 5], [2, 6], [3, 7]]) ➞ False
# Elements are overlapping, cannot be nested.
Notes
Sublists can be nested from smallest to largest or largest to smallest.
Elements must be strictly nested - e.g. no two lists can share either the same MAX or the same MIN (see example #3).
Sublists may not necessarily have unique elements (see example #1).
Sublists can be in any order (see example #2).
"""


def matryoshka(lst):
    for i in range(len(lst)-1):
        sub1 = lst[i]
        sub2 = lst[i + 1]

        if max(sub1) <= max(sub2) and min(sub1) <= min(sub2):
            return False
        if min(sub1) >= min(sub2) and max(sub1) >= max(sub2):
            return False
    return True

print(matryoshka([[7, 1], [7, 6, 5, 4, 3, 2], [6, 3], [4, 5]]))

print(matryoshka([[7, 1], [7, 6, 5, 4, 3, 2], [6, 3], [4, 5]]))

print(matryoshka([[4, 5], [6, 3], [7, 6, 5, 4, 3, 2], [8, 1]]))

print(matryoshka([[2, 2, 7], [3, 4, 5, 6], [4, 5]]))
