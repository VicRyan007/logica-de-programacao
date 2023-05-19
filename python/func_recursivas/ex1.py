def div(m,n):
    if m<n or n<=0:
        return 0
    else:
        return 1+div(m-n,n)
    

print(div(6,4))
print(div(10,2))