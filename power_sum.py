


def Power_Sum(X,N, current = 1):
    p = current**N
    if p > X:
        return 0 
    elif p == X:
        return  1
    else:
        return Power_Sum(X-p, N, current+1) + Power_Sum(X, N, current+1)



print(Power_Sum(100, 2))