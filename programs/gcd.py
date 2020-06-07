"""
ver: Python 3.x
Description: find the gcd of two numbers
@author: Saptarshi Das
"""

def gcd(m,n):
    fm = []                 #list of factors of m
    for i in range(1,m+1):
        if(m%i)==0:
            fm.append(i)

    fn = []                 #list of factors of n
    for j in range(1,n+1):
        if(n%j)==0:
            fn.append(j)

    cf = []                 #common factors of m and n
    for f in fm:
        if f in fn:
            cf.append(f)

    return (cf[-1])         #return the higest factor(rightmost)

result = gcd(4,12)
print ("GCD is: ",result)
