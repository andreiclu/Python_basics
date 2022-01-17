"""
There are three cups on a table, at positions A, B, and C.
At the start, there is a ball hidden under the cup at position B.
However, I perform several swaps on the cups, which is notated as two letters.
For example, if I swap the cups at positions A and B, I could notate this as AB or BA.
Create a function that returns the letter position that the ball is at, once I finish swapping the cups.
The swaps will be given to you as a list."""

def cup_swapping(swaps):
    pos = 'B'

    for i in swaps:
        if pos in i:
            pos = i.replace(pos,'')
    return pos



print(cup_swapping(["AC", "CA", "CA", "AC"]))

print(cup_swapping(["BA", "AC", "CA", "BC"]))

print(cup_swapping(["AB", "CA"]))