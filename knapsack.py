weight = [12,34,23,20]
value  = [10,200,300,70]

c = 50

dp = [[None for i in range(c+1)] for j in range(len(weight))]
# dynamic programming top down
def knapsak_top_down(c, w,v,dp,index):
    if c <= 0 or index ==  len(w):
        return 0

    if dp[index][c] != None:
        return dp[index][c]

    else:
        profit1 = 0
        if w[index] <= c:
            profit1 = v[index] + knapsak_top_down(c-w[index], w,v, dp,index+1)

        profit2 = knapsak_top_down(c,w,v,dp,index+1)

        dp[index][c] = max(profit1,profit2)

        return dp[index][c]
 
print(knapsak_top_down(c,weight,value,dp,0))

dp = [[0 for i in range(c+1)] for j in range(len(weight))]
#dynamic programming bottom up

def knapsak_bottom_up(c,w,v,dp):

    for i in range(len(w)):
        dp[i][0] = 0
    for i in range(c+1):
        if w[0] <= i:
            dp[0][i] = v[0]

    for i in range(1, len(w)):
        for j in range(1, c+1):
           profit1 = 0 
           if  j-w[i] >= 0:
               profit1 = v[i] + dp[i-1][j-w[i]]
           profit2 = dp[i-1][j]
           dp[i][j] = max(profit1, profit2)

    return dp[len(w)-1][c]


print(knapsak_bottom_up(c,weight,value,dp))

