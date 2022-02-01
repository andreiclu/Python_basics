"""Write a function that returns True if it is possible to build a string with a particular scrabble hand.

Examples
can_build("quavers", ["S", "U", "Q", "V", "A", "#", "#"]) ➞ True

can_build("move", ["M", "U", "T", "V", "E", "J", "#"]) ➞ True

can_build("move", ["M", "U", "T", "V", "E", "J", "S"]) ➞ False

can_build("sharp", ["S", "K", "H", "#", "#", "F", "F"]) ➞ False"""
import string
def can_build(word, lst):
    new_lst = []
    wild_tiles = ''
    for letter in lst:
        if letter in string.ascii_letters:
            new_lst.append(letter)
        else:
            wild_tiles += '#'
    missed_cnt = 0
    wild_tiles = wild_tiles.count('#')
    word = word.upper()
    for l in word:
        if l in lst:
            lst.remove(l)
        else:
            missed_cnt +=1
    if missed_cnt <= wild_tiles:
        return True
    else:
        return False


print(can_build("quavers", ["S", "U", "Q", "V", "A", "#", "#"]))

print(can_build("move", ["M", "U", "T", "V", "E", "J", "#"]))

print(can_build("move", ["M", "U", "T", "V", "E", "J", "S"]))

print(can_build("sharp", ["S", "K", "H", "#", "#", "F", "F"]))


