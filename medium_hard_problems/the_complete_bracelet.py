"""
A complete bracelet is a list with at least one subsequence (pattern) repeating at least two times, and completely -
the subsequence cannot be cut-off at any point. The subsequence must have length two or greater.

Complete bracelets:

[1, 2, 3, 3, 1, 2, 3, 3]  # Pattern: [1, 2, 3, 3]

[1, 2, 1, 2, 1, 2, 1, 2]  # Pattern: [1, 2] or [1, 2, 1, 2]

[1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7]  # Pattern: [1, 1, 6, 1, 1, 7]

[4, 4, 3, 4, 4, 4, 4, 3, 4, 4]  # Pattern: [4, 4, 3, 4, 4]
Incomplete bracelets:

[1, 2, 2, 2, 1, 2, 2, 2, 1]  # Incomplete (chopped off)

[1, 1, 6, 1, 1, 7]  # Incomplete (subsequence repeats only once)
Create a function that returns True if a bracelet is complete, and False otherwise.

Examples
complete_bracelet([1, 2, 2, 1, 2, 2]) ➞ True

complete_bracelet([5, 1, 2, 2]) ➞ False

complete_bracelet([5, 5, 5]) ➞ False
# potential pattern [5, 5] cut-off (patterns >= 2)


"""

def complete_bracelet(lst):
    if len(lst)%2!=0:
        return False
    lst_to_check = []

    for i in range(len(lst)):
        lst_to_check.append(lst[i])
        if list(lst_to_check) == lst[i+1:i+len(lst_to_check)+1] and len(lst_to_check) >=2:
            return True
    return False



    


print(complete_bracelet([1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7, 1, 1, 6, 1, 1, 7]))

print(complete_bracelet([1, 2, 1, 2, 1, 2, 1, 2]))

