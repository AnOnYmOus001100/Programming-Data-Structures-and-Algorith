"""
ver: using Python 3.x
Description: An optimized version of gcd, finds gcd of two numbers (no lists)
@author: Saptarshi Das
"""
def gcd_opt(m,n):
    for f in range(1,min(m,n)+1):
        if (m%f)==0 and (n%f)==0:
            cf = f

    return (cf)         #return the highest factor

print("GCD is: ",gcd_opt(3,9))
