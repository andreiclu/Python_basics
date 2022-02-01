"""
Create a function that returns the characters from a list or string r on odd or even positions, depending on the specifier s. The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).

Examples
char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 2nd & 4th positions

char_at_pos("EDABIT", "odd") ➞ "EAI"
# "E", "A" and "I" occupy the 1st, 3rd and 5th positions

char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd") ➞ ["A", "B", "T", "A", "I", "Y"]

"""

def char_at_pos(r, s):
    if s == 'odd':
        return r[::2] #list slicing from 0 to last in pairs of 2, that would means first element is odd, third is odd
    elif s == 'even':
        return r[1::2]
    else:
        raise Exception ("Please insert even or odd as paramenter two")


print(char_at_pos("EDABIT", "odd"))


print(char_at_pos([2, 4, 6, 8, 10], "even"))

print(char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd"))
