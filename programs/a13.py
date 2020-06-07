def g(m,n):
    res=0
    while m>=n:
        (res,m)=(res+1,m/n)
    return(res)
print(g(637,4))
