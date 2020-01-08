#method 1
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



# method 2 
def combinationalsum(x,s,i,r,result):
        if s == 0:
            result.append(r)
        else:
            if i<len(x):
                combinationalsum(x,s-x[i], i+1, r+[x[i]], result)
                combinationalsum(x, s, i+1, r, result)

x = [1,2,3,4,5,6]
s= 12
r = []
result = []
combinationalsum(x,s,0,r,result)
print(result)

        

    