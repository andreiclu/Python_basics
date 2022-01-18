

# divde and conquer algorithm
# breaks down problem into multple subproblems recrisvely util they
#become simple to solve
#Solution are combined to solve original problem

#Complexity: O(n*lon(n) running time
#Memory complexity: O(n)


#1. Split de array in half
#2. Call Merge Sort on each half to sort them recursively
#3. Merge both sorted halves into one sorted array

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i = 0 # left_arr inx
        j = 0 # right_arr index
        k = 0 # merged array index
        while i< len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+=1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        while j<len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1
    return arr

arr_test = [2,4,5,64,5,6,6,7,5,0]
print(merge_sort(arr_test))

