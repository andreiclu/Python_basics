"""
Hermione has come up with a precise formula for determining whether or not a phrase was ssspoken by a parssseltongue (a reference from the Harry Potter universe; the language of ssserpents and those who can converse with them).

Each word in a sssentence must contain either:

Two or more consecutive instances of the letter "s" (i.e. must be together ss..), or...
Zero instances of the letter "s" by itself.
Examples
is_parsel_tongue("Sshe ssselects to eat that apple. ") ➞ True

is_parsel_tongue("She ssselects to eat that apple. ") ➞ False
# "She" only contains one "s".

is_parsel_tongue("Beatrice samples lemonade") ➞ False
# While "samples" has 2 instances of "s", they are not together.

is_parsel_tongue("You ssseldom sssspeak sso boldly, ssso messmerizingly.") ➞ True
"""



def is_parsel_tongue(x):
    x = x.lower().split(" ")
    for i in range(len(x)):
        if 's' in x[i]:
            if not 'ss' in x[i]:
                return False
    return True




print(is_parsel_tongue("She ssselects to eat that apple. "))

print(is_parsel_tongue("Sshe ssselects to eat that apple. "))
