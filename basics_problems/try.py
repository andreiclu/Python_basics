
# import re
x = input("Insert a text:")

dict = {
    "COLEGIUL": "Co.",
    "LICEUL": "Li.",
    "NATIONAL": "Nat.",
    "TEORETIC": "Tr."
}
a = []
x = x.split()
for i in dict.values():
    if i in x:
        a.append(dict.keys())
print(a)



# my_set = ('COLEGIUL', 'LICEUL', 'NATIONAL', 'TEORETIC')

import re
from typing import List

"""
Se citeste un numar natural n si apoi n numere naturale. Afisati cate dintre ele au suma cifrelor egala cu numarul de lor de ordine de la citire.
Exemplu: n=6 si numerele 122 101 34 555 23 123
Se va afisa 3 deoarece numerele care respecta regula sunt 101 , 23 si 123.
"""

"""
A complete bracelet is a list with at least one subsequence (pattern) repeating at least two times, and completely - the subsequence cannot be cut-off at any point. The subsequence must have length two or greater.

Complete bracelets:

[1, 2, 3, 3, 1, 2, 3, 3]  # Pattern: [1, 2, 3, 3]

[1, 2, 1, 2, 1, 2, 1, 2]  # Pattern: [1, 2] or [1, 2, 1, 2]

[1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7]  # Pattern: [1, 1, 6, 1, 1, 7]

[4, 4, 3, 4, 4, 4, 4, 3, 4, 4]  # Pattern: [4, 4, 3, 4, 4]
"""


"""
Create a function that returns the smallest number of changes it takes to transform one number into one with identical digits. A step is incrementing or decrementing a digit by one.

Examples
smallest_transform(399) ➞ 6
# 399 transformed to 999 in 6 steps.

smallest_transform(1234) ➞ 4
# 1234 can be transformed to either 2222 or 3333 using 4 steps.

smallest_transform(153) ➞ 4

smallest_transform(33338) ➞ 5

smallest_transform(7777) ➞ 0
"""

