"""
Write a function that selects all words that have all the same vowels (in any order and/or number) as the first word,
including the first word.

Examples
same_vowel_group(["toe", "ocelot", "maniac"]) ➞ ["toe", "ocelot"]

same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]) ➞ ["many"]

same_vowel_group(["hoops", "chuff", "bot", "bottom"]) ➞ ["hoops", "bot", "bottom"]
"""

def same_vowel_group(w):
    f = set(w[0]) & set('aeiou')
    lst = []
    for i in w:
        if set(i) & set('aeiou') == f:
            lst.append(i)
    return lst


print(same_vowel_group(["hoops", "chuff", "bot", "bottom"]))

print(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]))

print(same_vowel_group(["toe", "ocelot", "maniac"]))

