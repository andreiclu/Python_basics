"""
Create a function that takes a list of any length. Modify each element (capitalize, reverse, hyphenate).

Examples
edit_words(["new york city"]) ➞ ["YTIC KR-OY WEN"]

edit_words(["null", "undefined"]) ➞ ["LL-UN", "DENIF-EDNU"]

edit_words(["hello", "", "world"]) ➞ ["OLL-EH", "-", "DLR-OW"]

edit_words([""]) ➞ ["-"]
"""


def edit_words(lst):
    for i in range(len(lst)):
        mid = len(lst[i]) // 2

        lst[i] = (lst[i][:mid] + '-' + lst[i][mid:]).upper()[::-1]

    return lst


print(edit_words(["11111", "999", "3333"]))

print(edit_words(["null", "undefined"]))

print(edit_words(["new york city"]))
