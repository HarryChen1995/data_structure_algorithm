import sys

def drop(total_egg, total_floor):
    look_table = [[0 for i in range(total_floor+1)] for y in range(total_egg+1)]
    

    # initialize table

    for i in range(1, total_floor+1):
        look_table[1][i] = i
    for i in range(1, total_egg+1):
        look_table[i][1] =1

    for i in range( 2, total_egg+1):
        for j in range(2, total_floor+1):
            look_table[i][j] = sys.maxsize


    

    for i in range( 2, total_egg+1):
        for j in range(2, total_floor+1):

            for n in range(2, j+1):
                worst_drop = 1+max(look_table[i-1][n-1], look_table[i][j-n]) # two case that agg break or not break

                if worst_drop < look_table[i][j]:
                    look_table[i][j] = worst_drop

    


    # return the global solution
    return look_table[total_egg][total_floor]





print(drop(2,36))


        
    



    
