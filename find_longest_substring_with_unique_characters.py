from collections import defaultdict

def lengthOfLongestSubstring(s):
    
    start, end = 0, 0
    max_length =-1
    hash_table=defaultdict(lambda:False,{})
    while start < len(s) and end < len(s):
        if hash_table[s[end]] == False:
            hash_table[s[end]]=True
            max_length = max(end-start+1, max_length)
            end +=1

        else:
             hash_table[s[start]] = False
             start +=1
    return max_length


print(lengthOfLongestSubstring("pwwkew"))