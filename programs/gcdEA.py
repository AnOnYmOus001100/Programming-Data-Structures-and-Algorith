"""
ver: using Python 3.x
Description: Most optimized version of gcd(iterativeway), find gcd of two numbers(Euclid's Algorithm)
@author: Saptarshi Das
"""
def gcd(m,n):
    #assume m>=n
    if (m<n):
        (m,n) = (n,m)

    while (m%n) != 0:
        (m,n) = (n,m%n)
    return n
    
