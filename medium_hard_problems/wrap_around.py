"""Wrap Around
Create a function to reproduce the wrap around effect shown:

Examples
wrap_around("Hello, World!", 2) ➞ "llo, World!He"

wrap_around("From what I gathered", -4) ➞ "eredFrom what I gath"

wrap_around("Excelsior", 30) ➞ "elsiorExc"

wrap_around("Nonscience", -116) ➞ "cienceNons"
Notes
The offset can be negative.
The offset can be greater than the length of string.
"""

def wrap_around(s,n):
    n = n % len(s)
    return s[n:]+s[:n]


print(wrap_around("Nonscience", -116))