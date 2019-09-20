def find_longest_common_consecutive_substring(s1,s2):
    
    look_table = [ [0]*(len(s1)+1) for i in range(len(s2)+1)]

    longest_s1_last_index = 0
    longest_length = 0
    for i in range(1,len(s2)+1):
        for j in range(1, len(s1)+1) :
            if s2[i-1] == s1[j-1]:
                look_table[i][j] = look_table[i-1][j-1] + 1
                if look_table[i][j] > longest_length:
                    longest_length = look_table[i][j]
                    longest_s1_last_index = j
            else:
                look_table[i][j] = 0 
    return (s1[longest_s1_last_index-longest_length:longest_s1_last_index],longest_length)

def find_longest_common_substring2(s1,s2):
    look_table = [ [0]*(len(s1)+1) for i in range(len(s2)+1)]

    longest_s1_last_index = 0
    longest_length = 0
    for i in range(1,len(s2)+1):
        for j in range(1, len(s1)+1) :
            if s2[i-1] == s1[j-1]:
                look_table[i][j] = look_table[i-1][j-1] + 1
        
            else:
                look_table[i][j] = max(look_table[i][j-1],look_table[i-1][j])
            
    return look_table[len(s2)][len(s1)]

        
                    





print(find_longest_common_substring2("ssdradpwrpswfp","ssdapwrpttmp"))
                    





print(find_longest_common_consecutive_substring("msdttp","gttgfemsdt"))