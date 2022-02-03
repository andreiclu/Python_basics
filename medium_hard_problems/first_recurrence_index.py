"""
Create a function that identifies the very first item that has recurred in the string argument passed. It returns the identified item with the index where it first appeared and the very next index where it resurfaced ⁠— entirely as an dictionary; or as an empty dictionary if the argument is either None, an empty string, or no recurring item exists.

Examples
recur_index("DXTDXTXDTXD") ➞ {"D": [0, 3]}
// D first appeared at index 0, resurfaced at index 3
// T appeared and resurfaced at indices 3 and 6 but D completed the cycle first

recur_index("YXZXYTUVXWV") ➞ {"X": [1, 3]}

recur_index("YZTTZMNERXE") ➞ {"T": [2, 3]}

recur_index("AREDCBSDERD") ➞ {"D": [3, 7]}

recur_index("") ➞ {}

recur_index(None) ➞ {}
"""

def recur_index(txt):
    if not txt:
        return {}
    lst = []
    for i,x in enumerate(txt):
        if not lst or x not in lst:
            lst.append(x)
        else:
            return{x:[lst.index(x), i]}
    return {}

print(recur_index("AREDCBSDERD"))

print(recur_index("YZTTZMNERXE"))


