import time
def linear_search(arr, k):
    for i ,val in enumerate (arr):
        if val == k:
            return (True, i)
    
    return (False,None)

def binary_search1(arr, left, right, k):
    if left > right:
        return (False, None)
     
    mid = left + (right-left)//2

    if arr[mid] == k:
            return (True, mid)
    
    elif k > arr[mid]:
        return binary_search1(arr, mid+1, right,k)
    
    else:
        return binary_search1(arr, left, mid-1,k)


def binary_search2(arr,data):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high-low)//2
        if  arr[mid] == data:
            return (True, mid)
        elif data < arr[mid]:
            high = mid-1
        else:
            low = mid+1
    return (False, None)


x = range(1, 10000) 
current_time = time.time()
print(binary_search1(x, 0, len(x)-1,6323))
print("binary_search1 takes {} seconds".format(time.time()-current_time))
current_time = time.time()
print(binary_search2(x,6323))
print("binary_search2 takes {} seconds".format(time.time()-current_time))
current_time = time.time()
print(linear_search(x,6323))
print("linear_search takes {} seconds".format(time.time()-current_time))
