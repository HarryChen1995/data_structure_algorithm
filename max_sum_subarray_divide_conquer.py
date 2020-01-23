def max_sum_cross_subarray(arr, low, mid, high):
    left_index = 0
    left_sum = float("-inf")
    sum = 0
    for i in reversed(range(low, mid+1)):
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
            left_index = i
    right_index = 0
    right_sum = float("-inf")
    sum = 0
    for i in range(mid+1, high+1):
        sum = sum + arr[i]
        if sum > right_sum:
            right_sum = sum 
            right_index = i
    return (left_index, right_index , left_sum + right_sum)

def max_sum_subarray(arr, low, high):

    if low == high:
        return (low, high, arr[low])

    mid = low + (high-low)//2

    (left_start, left_end, left_sum) = max_sum_subarray(arr, low, mid)
    (right_start, right_end, right_sum) = max_sum_subarray(arr, mid+1, high)
    (mid_start, mid_end, mid_sum) = max_sum_cross_subarray(arr, low, mid, high)

    if left_sum > right_sum  and left_sum > mid_sum:
        return (left_start, left_end, left_sum) 
    elif right_sum > left_sum and right_sum > mid_sum:
        return (right_start, right_end, right_sum)
    else:
        return (mid_start, mid_end, mid_sum)


x = [-2,1,4,2,199,-10,4,3,-2]
print(max_sum_subarray(x,0, len(x)-1))
