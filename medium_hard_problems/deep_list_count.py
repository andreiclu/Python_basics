"""
Create a function that takes a list and returns the number of ALL elements within it (including those within the sub-level list(s)).

Examples
deep_count([1, 2, 3]) ➞ 3

deep_count([[1], [2], [3]]) ➞ 6

deep_count(["x", "y", ["z"]]) ➞ 4

deep_count(["a", "b", ["c", "d", ["e"]]]) ➞ 7
"""

def deep_count(list_):
    count = 0
    for element in list_:
        if not isinstance(element,list):
            count = count+1
        elif isinstance(element,list):
            count = count+1
            count = count + deep_count(element)
    return count

print(deep_count(["a", "b", ["c", "d", ["e"]]]))