"""
Create a function that takes in parameter n and generates an n x n (where n is odd) concentric rug.

The center of a concentric rug is 0, and the rug "fans-out", as show in the examples below.

Examples
generate_rug(1) ➞ [
  [0]
]

generate_rug(3) ➞ [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]

generate_rug(5) ➞ [
  [2, 2, 2, 2, 2],
  [2, 1, 1, 1, 2],
  [2, 1, 0, 1, 2],
  [2, 1, 1, 1, 2],
  [2, 2, 2, 2, 2]
]

generate_rug(7) ➞ [
  [3, 3, 3, 3, 3, 3, 3],
  [3, 2, 2, 2, 2, 2, 3],
  [3, 2, 1, 1, 1, 2, 3],
  [3, 2, 1, 0, 1, 2, 3],
  [3, 2, 1, 1, 1, 2, 3],
  [3, 2, 2, 2, 2, 2, 3],
  [3, 3, 3, 3, 3, 3, 3]
]
"""
#
# def generate_row(x):
#     out = x //2
#     m = []
#     for i in range(x):
#         row = [0]*x # [x,x,x,x,...,x]
#         m.append(row)
#     for j in range(out):
#         val = out - j
#         ub = j
#         lb = x - j - 1
#         for k in range(ub, lb+1):
#             m[ub][k] = val
#             m[lb][k] = val
#             m[k][ub] = val
#             m[k][lb] = val
#
#     return m

# def generate_rug(n):
#     ret = []
#
#     for i in range(n):
#         ret.append([0] * n)
#         for j in range(n):
#             ret[i][j] = max(abs(n // 2 - i), abs(n // 2 - j))
#
#     return ret

def generate_rug(n):
    rug = [[n // 2 for i in range(n)] for j in range(n)]
    l = 1
    while (l <= n // 2):
        for i in range(l, n - l):
            for j in range(l, n - l):
                rug[i][j] = n // 2 - l
        l += 1

    return rug

print(generate_rug(7))
