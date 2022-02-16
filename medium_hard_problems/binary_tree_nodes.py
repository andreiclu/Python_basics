"""
Binary Tree Nodes
We have two lists _N and _P, where _N represents the value of a node in Binary Tree, and _P is the parent of _N.

N	P
1	2
3	2
6	8
9	8
2	5
8	5
5  -1
Write a function to find the node type of the node within this Binary Tree, ordered by the value of the node. Output one of the following:

Root: If node is root node.
Leaf: If node is leaf node.
Inner: If node is neither root nor leaf node.
Not exist: If node not exist.
node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 5) ➞ "Root"

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 6) ➞ "Leaf"

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 2) ➞ "Inner"

node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 10) ➞ "Not exist"
"""

def node_type(_N,_P, n):
    if n not in _N:
        return "Not exist"
    if _P[_N.index(n)] == -1:
        return "Root"
    if n not in _P:
        return "Leaf"
    return "Inner"


print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 2))

print((node_type([3, 2, 4, 9, 11, 10, 8, 5, 6, 7], [-1, 3, 3, 2, 3, 4, 4, 9, 10, 8], 10)))

print(node_type([1, 3, 6, 9, 2, 8, 5], [2, 2, 8, 8, 5, 5, -1], 10))