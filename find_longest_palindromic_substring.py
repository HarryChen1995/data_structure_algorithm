

def find_longest_palindromic_substr(s):
    n=len(s)
    if n == 0:
        return ""
    if n ==1:
        return s
    look_table = [[0 for x in range(n)] for y in range(n)]
    max_len  = 1


    i = 0
    while i < n:
        look_table[i][i] = True
        i =i + 1 
    
    
    
    
    start = 0
    i=0
    while i<n-1:
        if s[i] == s[i+1]:
            look_table[i][i+1] = True
            start = i
            max_len = 2
        i =i+1
    
    
    if  n >=3:

        k=3 

        while k <=n:
            i = 0 
            while i < n-k+1:
                j = i+k-1
                if look_table[i+1][j-1] and s[i]==s[j]:
                    look_table[i][j] =True
                    if k > max_len:
                        max_len = k
                        start = i
                i = i + 1
            k =k+1
    return s[start:start+max_len]




print(find_longest_palindromic_substr("abcda"))