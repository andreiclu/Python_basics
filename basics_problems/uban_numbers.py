"""
A number n is called uban if its name (in English) does not contain the letter "u". In particular, it cannot contain the terms "four", "hundred", and "thousand", so the uban number following 99 is 1,000,000.

Write a function to determine if the given integer is uban.

Examples
is_uban(456) ➞ False

is_uban(25) ➞ True

is_uban(1098) ➞ False
"""



def is_uban(st):
   if 99<st<=999999 or st== 14 or st == 4:
    return False
   elif "4" in str(st):
    if 40<=st<=49:
     return False
    else:
     return True
   else:
    return True

print(is_uban(156))