"""
Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).

Examples
vowel_links("a very large appliance") ➞ True

vowel_links("go to edabit") ➞ True

vowel_links("an open fire") ➞ False

vowel_links("a sudden applause") ➞ False
"""

import re
def vowel_links(txt):
    # a = txt.split()
    # vowels = 'aeiou'
    # for i in range(len(a)-1):
    #     if a[i][-1] in vowels and a[i+1][0] in vowels:
    #         return True
    # return False


    reg = re.findall(r'[aeiou] [aeiou]', txt)
    return bool(reg)


print(vowel_links("a sudden applause"))
print(vowel_links("go to edabit"))