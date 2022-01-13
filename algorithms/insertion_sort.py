


#Complexity: O(n^2)

def insertion_sort(list_a):
    index_len = range(1,len(list_a))
    for i in index_len:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i>0:
            list_a[i],list_a[i-1] = list_a[i-1],list_a[i]
            i = i-1

    return list_a



print(insertion_sort([7,45,765,5,454,33,44,3,3,43]))