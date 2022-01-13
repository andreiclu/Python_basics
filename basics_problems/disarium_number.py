"""
A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.

is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32

is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

is_disarium(544) ➞ False

is_disarium(518) ➞ True

is_disarium(466) ➞ False

is_disarium(8) ➞ True

"""


def is_disarium(num: int):
    lst_of_dig = []
    if num < 10:
        return 0
    new_num = num
    while new_num != 0:
        dig = new_num % 10
        lst_of_dig.append(dig)
        new_num = new_num // 10

    lst_of_dig.reverse()
    sum_of_dig = 0
    for i in range(1, len(lst_of_dig)+1):
        sum_of_dig += (lst_of_dig[i-1] ** i)
    if sum_of_dig == num:
            return True
    else:
        return False


#def is_disarium(n):
    # r = 0
    # for i in range(len(str(n))):
    #     r += int(str(n)[i]) ** (i + 1)
    # return r == n


print(is_disarium(518))
