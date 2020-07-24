s = ["apple", "pen"]
word = "applepenapple"

def wordbreak(s, word):
    dp = [None for i in range(len(word)+1)]
    dp[0] = True
    for i in range(0,len(word)):
        check = False
        for j in reversed(range(0,i+1)):
            if dp[j] == True and word[j:i+1] in s:
                check = True
                break
        dp[i+1] = check
    return dp[len(word)]


print(wordbreak(s,word))

