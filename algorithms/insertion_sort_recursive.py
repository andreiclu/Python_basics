


def insertion_recurisve(arr,i):
    #check if the array contains single item
    if i == 0:
        #then do nothing
        return
    #otherwise recursively sort array itrem upon index position i-1
    insertion_recurisve(arr,i-1)

    #let's define how it'll do the sorting
    j = i-1 #start goin down
    # at this point we'll be using a loop to goin down even further
    #untill some condtion exceed
    while j>0 and arr[j-1] > arr[j]:
        arr[j-1],arr[j] = arr[j], arr[j-1] #swap the values if the contion exceed
        j -=1 #decrementing j
    # finally the function will return sorted version of the input array
    return arr

a = [2,1,55,4,3,3,1,5,76,22]
i = len(a)

print(insertion_recurisve(a,i))