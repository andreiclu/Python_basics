"""
For this challenge, forget how to add two numbers together. The best explanation on what to do for this function is this meme:

https://knowyourmeme.com/memes/girl-at-whiteboard-adding

meme_sum(26, 39) ➞ 515
# 2+3 = 5, 6+9 = 15
# 26 + 39 = 515

meme_sum(122, 81) ➞ 1103
# 1+0 = 1, 2+8 = 10, 2+1 = 3
# 122 + 81 = 1103

meme_sum(1222, 30277) ➞ 31499
"""

def meme_sum(x, y):
    if max(x,y) == 0:
        return 0
    anw = ''
    while max(x,y) > 0:
        anw = str(x%10 + y%10) + anw
        x //=10
        y //=10

    return int(anw)


print(meme_sum(1222, 30277))