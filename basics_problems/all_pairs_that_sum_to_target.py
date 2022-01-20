"""Create a function that returns all pairs of numbers in a list that sum to a target. Sort the pairs in ascending order with respect to the smaller number, then order each pair in this order: [smaller, larger].

Examples
all_pairs([2, 4, 5, 3], 7) ➞ [[2, 5], [3, 4]]
# 2 + 5 = 7, 3 + 4 = 7

all_pairs([5, 3, 9, 2, 1], 3) ➞ [[1, 2]]

all_pairs([4, 5, 1, 3, 6, 8], 9) ➞ [[1, 8], [3, 6], [4, 5]]
# Sorted: 1 < 3 < 4; each pair is ordered [smaller, larger]"""

def all_pairs(lst, target):
	lst = sorted(lst)
	newlst = []
	for i, el1 in enumerate(lst):
		for el2 in lst[i+1:]:
			if el1+el2 == target:
				newlst.append([el1, el2])
	return newlst

print(all_pairs([4, 5, 1, 3, 6, 8], 9))