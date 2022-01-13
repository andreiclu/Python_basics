
#computational complexity O(n^2)
#memory complexity O(I) cuz i doesn't take other list to do it

# def bubble_sort(nums):
#     index_len = len(nums)-1
#     sorted = False
#
#     while not sorted:
#         sorted = True
#         for i in range(0,index_len):
#             if nums[i] > nums[i+1]:
#                 sorted = False
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#     return nums

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(0,n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-1):
            if arr[j]> arr[j+1]:

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            # if arr[j] > arr[j + 1]:
            #     arr[j], arr[j + 1] = arr[j + 1], arr[j]
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
    return arr



# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]


print(bubble_sort(arr))



