"""Write a function that returns True if exactly one word in the list differs in length from the rest. Return False in all other cases.

Examples
odd_one_out(["silly", "mom", "let", "the"]) ➞ True

odd_one_out(["swanky", "rhino", "moment"]) ➞ True

odd_one_out(["the", "them", "theme"]) ➞ False

odd_one_out(["very", "to", "an", "some"]) ➞ False"""

def odd_one_out(lst):
        res = []
        for i in lst:
            res.append(len(i))
        k = set(res)
        cnt = 0
        if len(k) > 2:
            return False
        else:
            for i in k:
                if res.count(i) > 1:
                    cnt += 1
            return cnt == 1


print(odd_one_out(["very", "to", "an", "some"]))

print(odd_one_out(["the", "them", "theme"]))

print(odd_one_out(["swanky", "rhino", "moment"]))

print(odd_one_out(["silly", "mom", "let", "the"]))


