


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

#
# def quick_sort(array, start, end):
#     if start >= end:
#         return
#
#     p = partition(array, start, end)
#     quick_sort(array, start, p-1)
#     quick_sort(array, p+1, end)
#
#
# # Quicksort Alrogithm
#
#
# def partition(array, start, end):
#     pivot = array[start]
#     low = start + 1
#     high = end
#
#     while True:
#         # If the current value we're looking at is larger than the pivot
#         # it's in the right place (right side of pivot) and we can move left,
#         # to the next element.
#         # We also need to make sure we haven't surpassed the low pointer, since that
#         # indicates we have already moved all the elements to their correct side of the pivot
#         while low <= high and array[high] >= pivot:
#             high = high - 1
#
#         # Opposite process of the one above
#         while low <= high and array[low] <= pivot:
#             low = low + 1
#
#         # We either found a value for both high and low that is out of order
#         # or low is higher than high, in which case we exit the loop
#         if low <= high:
#             array[low], array[high] = array[high], array[low]
#             # The loop continues
#         else:
#             # We exit out of the loop
#             break
#
#     array[start], array[high] = array[high], array[start]
#
#     return high
#
#
# array = [2, 8, 5, 3, 9, 4, 1]
#
# quick_sort(array, 0, len(array) - 1)
# print(array)