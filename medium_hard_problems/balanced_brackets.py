"""
Write a function that takes a string of brackets and checks whether they're balanced or not.

The sequence is balanced if:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also balanced.
Examples
isBalanced("{[()]}") ➞ True

isBalanced("[()]{}") ➞ True

 ➞ False
"""


def isBalanced(str_):
    if str_ == None: return None
    while len(str_):
        if str_.find('()') >= 0:
            str_ = str_.replace("()", "")
        elif str_.find('[]') >= 0:
            str_ = str_.replace("[]", "")
        elif str_.find('{}') >= 0:
            str_ = str_.replace("{}", "")
        else:
            return False  # if no matches, str wasn't balanced
    return True  # if while loop exits, str was balanced


print(isBalanced("{[([)]]}"))

print(isBalanced('{{[[([())]]]}}'))

print(isBalanced('[()]{}{[()()]()}'))