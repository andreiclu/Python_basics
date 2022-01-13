


#Complexity: O(n^2) worst case
#ave: O(n*long(n))

def quick_sort(seq):
    length = len(seq)
    if length <=1:
        return seq
    else:
        pivot = seq.pop()

    items_greater = []
    items_low = []

    for item in seq:
        if item > pivot:
            items_greater.append(item)

        else:
            items_low.append(item)

    return quick_sort(items_low) + [pivot] + quick_sort(items_greater)

print(quick_sort([2,4,5,5,656,7,76,45,45,24,24,22,11]))
