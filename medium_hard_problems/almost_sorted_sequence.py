"""
An almost-sorted sequence is a sequence that is strictly increasing or strictly decreasing if you remove a single element from the list (no more, no less). Write a function that returns True if a list is almost-sorted, and False otherwise.

For example, if you remove 80 from the first example, it is perfectly sorted in ascending order. Similarly, if you remove 7 from the second example, it is perfectly sorted in descending order.

Examples
almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41] ) ➞ True

almost_sorted([6, 5, 4, 7, 3]) ➞ True

almost_sorted([6, 4, 2, 0]) ➞ False
// Sequence is already sorted.

almost_sorted([7, 8, 9, 3, 10, 11, 12, 2]) ➞ False
// Requires removal of more than 1 item.
"""


def almost_sorted(lst):
    cnt = 0
    cnt2 = 0
    for i in range(1, len(lst)):
        if lst[i-1] < lst[i]:
            cnt+=1
        elif lst[i-1] > lst[i]:
            cnt2 +=1

    if cnt == len(lst)-2 and cnt2 == 1 or cnt2==len(lst)-2 and cnt == 1:
        return True
    else:
        return False

print(almost_sorted([6, 5, 4, 7, 3]))


print(almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41] ))

print(almost_sorted([5, 4, 3, 2, -1, 0]))

print(almost_sorted([6, 4, 2, 0]))

print(almost_sorted([9, 1, 8, 2, 7, 3]))