"""
Digits Battle!
Starting from the left side of an integer, adjacent digits pair up in "battle" and the larger digit wins. If two digits are the same, they both lose. A lone digit automatically wins.

Create a function that returns the victorious digits.

To illustrate:

battle_outcome(578921445) ➞ 7925
# [57]: 7 wins; [89] 9 wins; [21] 2 wins;
# [44] neither wins; 5 (automatically) wins
Examples
battle_outcome(32531) ➞ 351
# 3 deffeats 2, 5 defeats 3, 1 is a single.

battle_outcome(111) ➞ 1
# 1 and 1 tie, so neither move on, last 1 is a single.

battle_outcome(78925) ➞ 895
Notes
There are no winners in a battle with equal digits (neither should be printed).
If the length of the number is odd, the lone digit should be printed at the end of the number.
"""

def battle_outcome(num):
    str_num = str(num)
    new_str = ""
    if len(str_num)%2:
        str_num+='0'

    for i in range(0,len(str_num),2):
        if str_num[i]!=str_num[i+1]:
            new_str+=str(max(int(str_num[i]),int(str_num[i+1])))

    return int(new_str)


print(battle_outcome(578921445))

print(battle_outcome(32531))

print(battle_outcome(78925))

print(battle_outcome(111))