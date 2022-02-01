"""
Prietenul nostru, Ionci, a învățat la scoală despre ridicarea la putere. Ajutați-l să calculeze a^b.
"""

def power(a,b):
    if b == 0:
        return 1
    if b >=1:
        return a * power(a,b-1)


print(power(2,10))


