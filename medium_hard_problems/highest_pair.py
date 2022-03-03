"""
Highest Pair
You will be given a collection of five cards (representing a player's hand in poker).
If your hand contains at least one pair, return a list of two elements: True and the card number of the highest pair (trivial if there only exists a single pair). Else, return False.

Examples
highest_pair(["A", "A", "Q", "Q", "6" ]) ➞ [True, "A"]

highest_pair(["J", "6", "3", "10", "8"]) ➞ False

highest_pair(["K", "7", "3", "9", "3"]) ➞ [True, 3]

highest_pair(["K", "9", "10", "J", "Q"]) ➞ False

highest_pair(["3", "5", "5", "5", "5"]) ➞ [True, 5]
Notes
Hands with three or more of the same card still count as containing a pair (see the last example).
"""


def highest_pair(cards):
    a = {'J':11,'Q':12,'K':13,'A':14}
    b = [i for i in set(cards) if cards.count(i)>=2]

    if b:
        return[True, sorted(b, key=lambda x:int(x) if x.isdigit() else a[x])[-1]]
    return False



print(highest_pair(["3", "5", "5", "5", "5"]))

print(highest_pair(["K", "7", "3", "9", "3"]))

print(highest_pair(["J", "6", "3", "10", "8"]))