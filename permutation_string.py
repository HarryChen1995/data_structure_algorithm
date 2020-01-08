s = "abd"
def permutation(s, l, r, a):
    if l==r:
        a.append("".join(s))
    else:
        for i in range(l, r+1):
            s[l], s[i] = s[i], s[l]
            permutation(s,l+1, r,a)
            s[i], s[l] = s[l], s[i]



s = list(s)
a = []
permutation(s, 0, len(s)-1, a)
print(a)




