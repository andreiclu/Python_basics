"""
Rondo Form is a type of musical structure, in which there is a recurring theme/refrain, notated as A. Here are the rules for valid rondo forms:

Rondo forms always start and end with an A section.
In between the A sections, there should be contrasting sections notated as B, then C, then D, etc... No letter should be skipped.
There shouldn't be any repeats in the sequence (such as ABBACCA).
Create a function which validates whether a given string is a valid Rondo Form.

Examples
valid_rondo("ABACADAEAFAGAHAIAJA") ➞ True

valid_rondo("ABA") ➞ True

valid_rondo("ABBACCA") ➞ False

valid_rondo("ACAC") ➞ False

valid_rondo("A") ➞ False
"""

def valid_rondo(s):
    a = s[1:-1].split('A')

    if s[0] == s[-1] == 'A' and a[0]=='B' and a == sorted(a):
        return True
    else:
        return False


print(valid_rondo("ABACADAEAFAGAHAIAJA"))


print(valid_rondo("ABBACCA"))

print(valid_rondo("ACAC"))

print(valid_rondo("ABA"))