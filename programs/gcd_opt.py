"""
ver: using Python 3.x
Description: An optimized version of gcd, finds gcd of two numbers
@author: Saptarshi Das
"""
def gcd_opt(m,n):
    cf = []                 #common factors of m and n
    for f in range(1,min(m,n)+1):
        if (m%f)==0 and (n%f)==0:
            cf.append(f)

    return (cf[-1])         #return the highest factor(rightmost)

print("GCD is: ",gcd_opt(4,6))
