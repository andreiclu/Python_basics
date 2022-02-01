"""
Create a function that takes in two words as input and returns a list of three elements, in the following order:

Shared letters between two words.
Letters unique to word 1.
Letters unique to word 2.
Each element should have unique letters, and have each letter be alphabetically sorted."""


def letters(word1,word2):
    shared = ''.join(sorted(set(x for x in word1 if x in word2)))
    w1 = ''.join(sorted(set(x for x in word1 if x not in word2)))
    w2 = ''.join(sorted(set(x for x in word2 if x not in word1)))
    return [shared, w1, w2]

print(letters("sharp", "soap"))
print(letters("board", "bored"))


