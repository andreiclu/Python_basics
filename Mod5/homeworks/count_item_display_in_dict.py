from collections import Counter

def CountFrequency(lst):
    dict = {}
    for item in lst:
        if (item in dict):
            dict[item] += 1
        else:
            dict[item] = 1

    for key, value in dict.items():
        print(f"{key}:{value}")



print(CountFrequency([1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]))


def CountFrequency_with_methods(my_list):
    count = {}
    for i in my_list:
        count[i] = count.get(i, 0) + 1
    return count


print(CountFrequency_with_methods([1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]))



def CountFreq_with_another_method(my_lst):
    d = dict(Counter(my_lst))
    return d

a = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

print(CountFreq_with_another_method(a))