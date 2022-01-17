"""
Find the index of a string within a hex encoded string.

You will be given a string which needs to be found in another string which has previously been translated into hex.
You will need to return the first index of the needle within the hex encoded string.
"""
import codecs
def first_index(hex_txt, word):
    spl_txt = list(hex_txt.split())
    enc_word = codecs.encode(word.encode(encoding='utf-8'), 'hex')
    for ind, i in enumerate(spl_txt):
        if i == str(enc_word)[2:4]:
            return ind


print(first_index("47 6f 6f 64 62 79 65 20 77 6f 72 6c 64", "world"))

print(first_index("68 65 6c 6c 6f 20 77 6f 72 6c 64", "world"))
