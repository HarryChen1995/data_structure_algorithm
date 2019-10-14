

def combinational_sum(arr, Sum, result, start, r):
    if Sum ==0:
        result.append(r)

    for i in range(start, len(arr)):
        if Sum - arr[i]>=0:
            combinational_sum(arr,Sum-arr[i], result,i,r+[arr[i]])






def find_combinational_sum(arr, s):
    arr = sorted(list(set(arr)))
    result = []

    combinational_sum(arr,s,result,0,[])

    return result



print(find_combinational_sum([2,4,6,8],10))
