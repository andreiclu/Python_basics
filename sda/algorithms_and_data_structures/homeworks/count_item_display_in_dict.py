

"""
Count the occurrences of each item and display them in a dictionary. Also, as a second method, solve this using Python functions.
Test Data:  [11, 45, 8, 11, 23, 45, 23, 45, 89]
Expected Result: {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
"""



from collections import Counter

def CountFrequency(lst):
    dict = {}
    for item in lst:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1
    return dict


print(CountFrequency([11, 45, 8, 11, 23, 45, 23, 45, 89]))


def CountFrequency_with_methods(my_list):
    count = {}
    for i in my_list:
        count[i] = count.get(i, 0) + 1
    return count


print(CountFrequency_with_methods([11, 45, 8, 11, 23, 45, 23, 45, 89]))



def CountFreq_with_another_method(my_lst):
    d = dict(Counter(my_lst))
    return d

a = [11, 45, 8, 11, 23, 45, 23, 45, 89]

print(CountFreq_with_another_method(a))


def CountFreq_with_yet_another_method(list_):
    count = {}
    for elem in set(list_):
        count[elem] = list_.count(elem)
    return count

print(CountFreq_with_yet_another_method([11, 45, 8, 11, 23, 45, 23, 45, 89]))
