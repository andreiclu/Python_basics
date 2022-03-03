"""
Musical Instrument Note Ranges
Musical instruments have a range of notes to play, some instruments having a much larger range than others.

Given the following ranges for the instrument, create a function that returns True if a given note is within a given instrument's range. Otherwise, return False.

Instrument	Range
Piccolo	D4-C7
Tuba	D1-F4
Guitar	E3-E6
Piano	A0-C8
Violin	G3-A7
Examples
instrument_range("Piccolo", "A3") ➞ False

instrument_range("Violin", "G6") ➞ True

instrument_range("Piano", "C8") ➞ True
Notes
Tests will only include natural notes (i.e. you will only deal with letters and numbers, no special characters).
The musical scale follows this pattern: ... A1, B1, C1, D1, E1, F1, G1, A2, B2 ...
You don't need to worry about invalid inputs.
"""

def instrument_range(instr, note):
    d = {
        "Piccolo": [31, 51],
        "Tuba": [10, 33],
        "Guitar": [25, 46],
        "Piano": [0, 58],
        "Violin": [27, 49],
    }
    arr = []
    l = 'ABCDEFG'

    for i in range(10):
        for j in range(len(l)):
            arr.append(str(l[j]+str(i)))
    return arr.index(note)>=d[instr][0] and arr.index(note)<=d[instr][1]




print(instrument_range("Piccolo", "A3"))

print(instrument_range("Violin", "G6"))

print(instrument_range("Piano", "C8"))
