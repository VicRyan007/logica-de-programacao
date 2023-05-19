def exp(x,n):
    if n==0:
        return 1
    if x==0:
        return 0
    else:
        return x*exp(x,n-1)
    
print(exp(2,2))
