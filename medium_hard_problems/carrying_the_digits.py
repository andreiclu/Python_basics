"""
Carrying the Digits
Write a function that returns the number of times you must carry a digit when you sum together two integers.

Examples
carry_digits(36, 135) ➞ 1
# You carry the 1 when you sum 6 and 5 together.

carry_digits(671, 329) ➞ 3

carry_digits(1111, 3333) ➞ 0

carry_digits(53214, 56905) ➞ 3
Notes
Count all carry operations (even those on leading digits).
"""


def carry_digits(x, y):
    count = 0
    carry = 0

    while x > 0 and y > 0:
        carry = (carry + (x % 10) + (y % 10)) // 10
        count += 1 if carry > 0 else 0
        x //= 10
        y //= 10
    return count


print(carry_digits(53214, 56905))
