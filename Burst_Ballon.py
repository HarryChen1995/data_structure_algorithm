def burst_ballon(arr):


    table = [ [0 for i in arr] for j in arr ]
    for L in reversed(range(len(arr))):
        for R in range(L, len(arr)):
            for i in range(L, R+1):
                left_L  = arr[L-1] if L else 1
                right_R =  1 if R == len(arr)-1 else arr[R+1]
                right_part = table[L][i-1] if L<= i-1 else 0
                left_part = table[i+1][R]  if i+1 <= R else 0
                s = arr[i]*left_L * right_R+right_part  +  left_part
                table[L][R] = max(table[L][R],s)
    
    return table [0][len(arr)-1]





print(burst_ballon([3,1,5,8]))