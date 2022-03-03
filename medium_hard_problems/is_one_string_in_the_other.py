"""
Is One String in the Other?
Create a function that takes two strings and returns True if either of the strings appears at the very end of the other string.
Return False otherwise. The character * is a wildcard, so it can take the place of any character.

Examples
overlap("ABC", "Ican'tsingmyABC") ➞ True

overlap("abc", "Ican'tsingmyABC") ➞ True

overlap("Ican'tsingmyABC", "abc") ➞ True

overlap("hello world", "hello") ➞ False

overlap("+=", "this should work too +=") ➞ True

overlap("hey", "*********") ➞ True
"""


def overlap(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()

    lstr1 = len(str1)
    lstr2 = len(str2)
    flg = True

    if lstr1 >=lstr2:
        for i in range(lstr2):
            if str2[i]!=str1[lstr1-lstr2+i] and str1[lstr1-lstr2+i]!='*' and str2[i]!='*':
                flg=False
    if lstr2>=lstr1:
        for i in range(lstr1):
            if str1[i]!=str2[lstr2-lstr1+i] and str2[lstr2-lstr1+i]!='*'and str1[i]!='*':
                flg=False
    return flg


print(overlap("+=", "this should work too +="))

print(overlap('hey','********'))

print(overlap("hello world", "hello"))