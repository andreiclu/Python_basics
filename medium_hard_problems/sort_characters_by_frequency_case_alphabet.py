"""
The function is given a string. Sort the characters and return a new string. Sorting conditions:

Most frequent move in front.
For the same frequency upper case characters move in front.
For the same frequency and case sort them alphabetically.
Examples
frequency_sort("tree") ➞ "eert"

frequency_sort("cccaaa") ➞ "aaaccc"

frequency_sort("Aabb") ➞ "bbAa"
"""

def frequency_sort(txt):
    return ''.join(sorted(txt, key=lambda x: (-txt.count(x), x.islower(),x)))

print(frequency_sort("cccaaa"))

print(frequency_sort("tree"))
