def h(n):
    s=0
    for i in range(2,n):
        if (n%i)==0:
            s = s+i
    return(s)

print(h(36)-h(34))
