"""
Write a function that sorts the words in a given string lexicographically (lexical sort) and by length in reverse order.

Examples
reverse_sort("You've rocked the pragmatic world in the making!")
 ➞ "pragmatic making! You've rocked world the the in"

reverse_sort("Tesh makes my world worth enjoying and living for.")
 ➞ "enjoying living worth world makes Tesh for. and my"

reverse_sort("Shaken by the bloody truth and crazy lies.")
 ➞ "Shaken bloody truth lies. crazy the and by"

reverse_sort("Programming in Python is a lot of fun.")
 ➞ "Programming Python fun. lot of is in a"
Notes
Special characters, punctuation marks and symbols are part of the word that directly precedes it.
The space character separates each word in the given string.
Case insensitive sorting is required.
"""

def reverse_sort(seq):
    s = seq.split()
    s = sorted(s, key=lambda x:x.lower(), reverse=True)
    s = sorted(s, key=lambda x:len(x), reverse=True)
    return " ".join(s)

print(reverse_sort("Shaken by the bloody truth and crazy lies."))

print(reverse_sort("Tesh makes my world worth enjoying and living for."))