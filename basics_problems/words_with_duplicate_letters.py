"""
Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.

Examples
no_duplicate_letters("Fortune favours the bold.") ➞ True

no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True

no_duplicate_letters("Look before you leap.") ➞ False
# Duplicate letters in "Look" and "before".

no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
# Duplicate letters in "apple", "keeps", "doctor", and "away".
"""

def no_duplicate_letters(phrase):
	for word in phrase.split():
		temp = []
		for ch in word:
			if ch not in temp:
				temp.append(ch)
			else:
				return False
	return True

print(no_duplicate_letters("Look before you leap."))

print(no_duplicate_letters("Fortune favours the bold."))