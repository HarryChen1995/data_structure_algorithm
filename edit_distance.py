

def Edit_Distance(s1, s2):
    table = [[ 0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]


    for i in range(1, len(s1)+1):
        table[0][i] = i
    for i in range(1, len(s2)+1):
        table[i][0] = i
    

    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            if s2[i-1] == s1[j-1]:
                table[i][j] = table[i-1][j-1]

            else:
                table[i][j] = min(table[i-1][j-1], table[i-1][j], table[i][j-1])+1
        

    return table[len(s2)][len(s1)]



print(Edit_Distance("sunday","saturday"))

    