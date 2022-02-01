"""
Given a string text. Write a function that returns the character with the highest frequency. If more than 1 character has the same highest frequency, return all those characters as an array sorted in ascending order. If there is no repetition in characters, return "No Repetition".

Examples
max_occur("Computer Science") ➞ ['e']

max_occur("Edabit") ➞ "No Repetition"

max_occur("system admin") ➞ ['m', 's']

max_occur("the quick brown fox jumps over the lazy dog") ➞ [' ']
"""

def max_occur(txt):
    count = {}
    rez = []
    for i in txt:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    for k,v in count.items():
        if v==max(count.values()):
            rez.append(k)
    return rez if len(rez)!=len(txt) else 'No Repetition'
print(max_occur("Computer Science"))

print(max_occur("system admin"))