import numpy as np


def rotation_matrix(matrix):

    level = len(matrix)

    for layer in range(level//2):
        first , last = layer , level - layer -1

        for i in range(first, last):

            # save top
            top = matrix[layer][i]

            # move left to top 
            matrix[layer][i] = matrix[-i-1][layer]

            # move bottom to left
            matrix[-i-1][layer]=matrix[last][-i-1] 
            
            #move right to bottom

            matrix[last][-i-1] = matrix[i][last]

            # copy  top to right
            matrix[i][last] = top

    



matrix = [ [1, 2, 3, 4,  5],
           [6, 7, 8, 9, 10],
           [11,12,13,14,15],
           [16,17,18,19,20],
           [21,22,23,24,25]]

print("original matrix:")
print(np.array(matrix))
rotation_matrix(matrix)
print("after rotate 90 degree clockwise:")
print(np.array(matrix))