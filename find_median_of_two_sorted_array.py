import sys
def median(arr1, arr2):
    if len(arr1)<len(arr2):
        arr_x = arr1
        arr_y= arr2
    else:
        arr_x = arr2
        arr_y = arr1
    
    even = False
    if  (len(arr1)+ len(arr2)) %2 ==0:
        even = True
    start = 0
    end = len(arr_x)
    while start <=end:


        dis_x = (start + end)//2
        dis_y = (len(arr1)+len(arr2)+1)//2 - dis_x
        maxleft_x = -sys.maxsize if dis_x ==0 else arr_x[dis_x-1]
        minright_x = sys.maxsize if dis_x == len(arr_x) else arr_x[dis_x]

        maxleft_y = -sys.maxsize if dis_y ==0 else arr_y[dis_y-1]
        minright_y = sys.maxsize if dis_y == len(arr_y) else arr_y[dis_y]

        if maxleft_x <=  minright_y and maxleft_y <= minright_x:
            if even:
                return (max(maxleft_x,  maxleft_y ) + min( minright_x, minright_y))/2
            else:
                return max(maxleft_x,  maxleft_y )
            
        elif maxleft_x > minright_y:

            end = dis_x -1
            
        else:
                start = dis_x +1



print(median([1,2],[3,4]))


    