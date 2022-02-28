"""COUNT_NGRAMS
Define a function that takes a sequence and returns the bigram frequencies.
Bigrams are pairs of consecutive symbols. The sequence "ababc" has 3 unique bigrams, "ab", "ba" and "bc".
The frequency of "ab" is 2, the others occur once.
Choose an appropriate data structure for the frequencies. Do not use the collections Python module.
Type hints are a plus. Write tests for your function and test a few corner cases."""

import unittest
def bigram(s):
    d={}
    for i in range(len(s)-1):

        ss = (s[i]+s[i+1])
        d[ss]=d.get(ss,0)+1


    return d


