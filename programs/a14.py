def mys(m):
    if m==1:
        return(1)
    else:
        return(m+mys(m-1))

print(mys(5))
