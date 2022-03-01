"""
Digital Division
In this challenge, you have to verify if a number is exactly divisible by a combination of its digits. There are three possible conditions to test:

The given number is exactly divisible by each of its digits excluding the zeros.
The given number is exactly divisible by the sum of its digits.
The given number is exactly divisible by the product of its digits.
Given an integer n, implement a function that returns:

If every test is true, a string "Perfect".
If some test is true, the number of true tests (1 or 2).
If every test is false, a string "Indivisible".
Examples
digital_division(21) ➞ 1
# Exactly divisible only by the sum of its digits (2 + 1 = 3).

digital_division(128) ➞ 2
# Exactly divisible by each of its digits.
# Exactly divisible by the product of its digits (1 * 2 * 8 = 16).

digital_division(100) ➞ 2
# Exactly divisible by each of its digits (excluding zeros).
# Exactly divisible by the sum of its digits (1 + 0 + 0 = 1).

digital_division(12) ➞ "Perfect"
# Exactly divisible by each of its digits.
# Exactly divisible by 3 (sum of digits = 1 + 2).
# Exactly divisible by 2 (product of digits = 1 * 2).

digital_division(31) ➞ "Indivisible"
# Every testing condition is false.
Notes
Remember to exclude any 0-digit when testing if the given n is divisible by each of its digits (see example #3).
A number containing at least a 0-digit can't be exactly divided by the product of its digits (division by 0).
Trivially, every single-digit positive number greater than 0 is Perfect
Any given number will be a positive integer greater than 0.
"""


def digital_division(n):
    count = 0
    prod_ = 1
    flg = 0
    lst = [int(i) for i in str(n)]
    sum_ = sum(lst)
    for j in lst:
        prod_ *= j

    if all(not n%i for i in lst if i!=0):
        count +=1
    if not n%sum_:
        count+=1
    if prod_!= 0 and not n%prod_:
        count+=1

    if count == 3:
        return "Perfect"
    elif count ==0:
        return "Indivisible"
    else:
        return count


print(digital_division(666))
print(digital_division(31))
print(digital_division(735))
print((digital_division(123456789)))
print(digital_division(100))