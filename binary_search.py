import time
def linear_search(arr, k):
    for i ,val in enumerate (arr):
        if val == k:
            return (True, i)
    
    return (False,None)

def binary_search(arr, left, right, k):
    if left > right:
        return (False, None)
     
    mid = left + (right-left)//2

    if arr[mid] == k:
            return (True, mid)
    
    elif k > arr[mid]:
        return binary_search(arr, mid+1, right,k)
    
    else:
        return binary_search(arr, left, mid-1,k)





x =  [1,2,3,4,4,10]
current_time = time.time()
print(binary_search(x, 0, len(x)-1,4))
print("binary_search takes {} seconds".format(time.time()-current_time))