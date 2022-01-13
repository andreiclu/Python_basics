



def bubble_sort_recur(a, i, j, n):
    if j == n:
        i = i+1
        j = 0
    if i == n:
        return
    if a[i] < a[j]:
        temp = a[j]
        a[j] = a[i]
        a[i] = temp
        bubble_sort_recur(a, i, j+1, n);
    else:
        bubble_sort_recur(a, i, j + 1, n);
    return a


mylist = [64,34,24,12,22,11,90]

print(bubble_sort_recur(mylist,0,0,len(mylist)))