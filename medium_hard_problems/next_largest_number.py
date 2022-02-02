"""
Write a function that returns the next number that can be created from the same digits as the input.

Examples
next_number(19) ➞ 91

next_number(3542) ➞ 4235

next_number(5432) ➞ 5432

next_number(58943) ➞ 59348
"""


from itertools import permutations

def next_number(n):
    if n<10:
        return n
    nn = list(str(n))
    comb = permutations(nn)
    lst = []
    for i in comb:
        v = int(''.join(map(str, i)))
        if v not in lst:
            lst.append(v)
    lst.sort()
    for j in range(len(lst)):
        if lst[j] == n:
            return lst[j+1]

print(next_number(899))

# def next_number(n):
#     if n<10:
#         return n
#     nn = str(n)
#     comb = sorted(set(permutations(nn,len(nn))))
#     idx = comb.index(tuple(nn))
#     if idx != len(comb)-1:
#         return int(''.join(comb[idx+1]))
#     else:
#         return n

print(next_number(58943))


print(next_number(3524))