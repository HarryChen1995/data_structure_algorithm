
def find_max_contiguous_subarray_sum(arr):
    max_sum_table = [0] * len(arr)

    for i in range(len(arr)):
        if i  == 0:
            max_sum_table[i] = arr[i]
        else:

            max_sum_table[i] = max(arr[i], max_sum_table[i-1]+arr[i])
        
    end_index = max_sum_table.index(max(max_sum_table))
    start_index = 0
    for i in reversed(range(end_index+1)):
        if max_sum_table[i] < 0:
            start_index = i+1
            break
            
    return (max(max_sum_table),start_index,end_index)



x = [-2,1,4,2,199,-10,4,3,-2]
print(" the max sum of contiguous subarray of {} is:".format(x))
print(find_max_contiguous_subarray_sum(x))



matrix =      [[ 6,-5,-7, 4,-4],
               [-9, 3,-6, 5, 2],
               [-10,4, 7,-6, 3],
               [-8, 9,-3, 3,-7]]



def find_max_sub_matrix(matrix):
    max_sum = -1000
    left_index = 0
    right_index = 0
    top_index = 0
    bottom_index =0
    for l in range(len(matrix[0])):
        running_row_sum = [0] * len(matrix)
        for r in range(l,len(matrix[0])):
            
            for  i in range(len(matrix)):
                running_row_sum[i] = matrix[i][r] +running_row_sum[i]
            temp_sum, top, bottom = find_max_contiguous_subarray_sum(running_row_sum)
            if temp_sum >= max_sum:
                top_index = top
                bottom_index = bottom
                left_index = l
                right_index =r
                max_sum = temp_sum


    return (max_sum, left_index, right_index, top_index, bottom_index)

print(find_max_sub_matrix(matrix))