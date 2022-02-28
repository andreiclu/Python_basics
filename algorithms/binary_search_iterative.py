"Binary search iterative way"

def binary_search(seq, item):
    begin_index = 0
    end_index = len(seq)-1

    while begin_index <= end_index:
        mid = begin_index + (end_index - begin_index) // 2
        mid_val = seq[mid]
        if mid_val == item:
            return mid
        elif item < mid_val:
            end_index = mid - 1

        else:
            begin_index = mid+1
    return None

seq_a = [2,4,5,6,7,8,9,10,12,14,15,16]
item_a = 12

print(binary_search(seq_a,item_a))

# Complexity

# n * 1/2 * 1/2 *...* 1/2 = n/2^k
# k = log2n sau O(log(n))











