
def find_longest_increase_sequence(arr):
    LIS = [1] * len(arr)
    i = 0 
    j = 1

    while j < len(arr):
        for i  in range (j):
            if arr[i] < arr[j] :
                LIS[j] = max(LIS[i]+1, LIS[j])
        j += 1
    

    return max(LIS)




print("the longest increase subsequence of list {} is :".format([1,2,2,3,4,5,6,1,10,9,20,21,11,23,1,2,3,24]))
print(find_longest_increase_sequence([1,2,2,3,4,5,6,1,10,9,20,21,11,23,1,2,3,24]))
