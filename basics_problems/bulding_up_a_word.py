"""
You are given an input list of strings, ordered by ascending length.

Write a function that returns True if, for each pair of consecutive strings, the second string can be formed from the first by adding a single letter either at the beginning or end.

Examples
can_build(["a", "at", "ate", "late", "plate", "plates"]) ➞ True

can_build(["a", "at", "ate", "late", "plate", "plater", "platter"]) ➞ False
# "platter" is formed by adding "t" in the middle of "plater"

can_build(["it", "bit", "bite", "biters"]) ➞ False
# "biters" is formed by adding two letters - we can only add one

can_build(["mean", "meany"]) ➞ True


"""

def can_build(lst):

    for i in range(len(lst)-1):
        if lst[i] not in lst[i+1] or len(lst[i])+1 != len(lst[i+1]):
            return False

    return True

print(can_build(["it", "bit", "bite", "biters"]))

print(can_build(["a", "at", "ate", "late", "plate", "plates"]))

print(can_build(["a", "at", "ate", "late", "plate", "plater", "platter"]))