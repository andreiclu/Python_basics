"""
Write a function that takes a list of 11 integers and returns a string in a phone number format.
"""

from typing import List

def create_phone_number(n: List[int]) -> str:
    phone_number = '+('
    for i, num in enumerate(n):
        if i < 3:
            phone_number += str(num)
            if i == 1:
                phone_number += ') '
        elif i <= 12:
            phone_number += str(num)
            if i == 4 or i ==7:
                phone_number += '-'
    return phone_number
print(create_phone_number([1,2,3,4,5,6,7,8,9,3,4]))

