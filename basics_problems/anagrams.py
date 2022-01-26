"""
Write a function that finds all the anagrams of a given word from the list provided. Words found should be return as a list.
"""

from typing import List

def anagram(word: str, lst_of_words: List[str]) -> List[str]:
    word_s = sorted(word)
    list_of_ana = []
    for i in lst_of_words:
        if word_s == sorted(i):
            list_of_ana.append(i)
    return list_of_ana

print(anagram('rac', ['car', 'girl', 'tofu', 'rca', 'macara']))



