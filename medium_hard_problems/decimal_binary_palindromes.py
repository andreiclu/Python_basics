"""
Decimal and Binary Palindromes
A number/string is a palindrome if the digits/characters are the same when read both forward and backward.
Examples include "racecar" and 12321. Given a positive number n, check if n or the binary representation of n is palindromic. Return the following:

"Decimal only." if only n is a palindrome.
"Binary only." if only the binary representation of n is a palindrome.
"Decimal and binary." if both are palindromes.
"Neither!" if neither are palindromes.
Examples
palindrome_type(1306031) ➞ "Decimal only."
# decimal = 1306031
# binary  = "100111110110110101111"

palindrome_type(427787) ➞ "Binary only."
# decimal = 427787
# binary  = "1101000011100001011"

palindrome_type(313) ➞ "Decimal and binary."
# decimal = 313
# binary  = 100111001

palindrome_type(934) ➞ "Neither!"
# decimal = 934
# binary  = "1110100110"
"""




def is_pal(x):
    w = ""
    for i in str(x):
        w = i + w
    if (x == w):
        return 1
    else:
        return 0

def dec_to_bin(d):
    binary_str = ''
    d = int(d)
    while d>0:
        r = d % 2
        if r == 1:
            binary_str = '1' + binary_str
            d = d//2
        else:
            binary_str = '0' + binary_str
            d = d//2
    return binary_str

def palindrome_type(n):
    n = str(n)
    if is_pal(n) and is_pal(dec_to_bin(n)):
        return "Decimal and binary"
    elif is_pal(n):
        return "Decimal only"
    elif is_pal(dec_to_bin(n)):
        return "Binary only"
    else:
        return "Neither!"


print(palindrome_type(1306031))
print(palindrome_type(427787))
print(palindrome_type(313))
print(palindrome_type(934))

