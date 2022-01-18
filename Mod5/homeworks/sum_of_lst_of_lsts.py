



new_lst = []
def get_all_as_lst(a):
    for i in a:
        if isinstance(i,list):
            for j in i:
                new_lst.append(j)
        else:
            new_lst.append(i)
    return new_lst

def sum_iter(x):
    sum = 0
    for i in get_all_as_lst(x):
        sum += i
    return sum

a = [1, 2, [3,4], [5,6]]
print(sum_iter(a))

# def sum_rec(x):
#     if len(x):
#         return get_all_as_lst(a)[0] + sum_rec(get_all_as_lst(a))[1:]
#     else:
#         return
#
#

def sum_rec(x):
    sum = 0

    for i in range(len(x)):
        if type(x[i]) == list:
            sum += sum_rec(x[i])
        else:
            sum += x[i]
    return sum
a = [1, 2, [3, 4], [5, 6]]
print(sum_rec(a))
