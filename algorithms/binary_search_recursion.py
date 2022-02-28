
def binary_search(data,low, high, item):
    if low <= high:
        middle = (low+high)//2

        if data[middle] == item:
            return middle
        elif item < data[middle]:
            return binary_search(data,low, middle-1,item)
        else:
            return binary_search(data, middle+1, high, item)
    else:
        return -1




numbers = [3,5,6,7,8,9,12,15,23,155]

print(binary_search(numbers, 0, len(numbers)-1, 12))

