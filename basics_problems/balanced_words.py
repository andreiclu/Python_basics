"""
We can assign a value to each character in a word, based on their position in the alphabet (a = 1, b = 2, ... , z = 26). A balanced word is one where the sum of values on the left-hand side of the word equals the sum of values on the right-hand side. For odd length words, the middle character (balance point) is ignored.

Write a function that returns True if the word is balanced, and False if it's not.

Examples
balanced_word("zips") ➞ True
# "zips" = "zi|ps" = 26+9|16+19 = 35|35 = True

balanced_word("brake") ➞ False
# "brake" = "br|ke" = 2+18|11+5 = 20|16 = False
"""

def balanced_word(word):
    dict_of_letter = {
        ' ': 0,
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
    }
    s1,s2 = 0,0
    for i in range(0,int(len(word)/2)):
        s1+= dict_of_letter[word[i]]
        s2+= dict_of_letter[word[-(i+1)]]

    return s1==s2


print(balanced_word("zips"))

print(balanced_word("brake"))

print(balanced_word('anesthesiologies'))