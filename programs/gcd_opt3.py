"""
ver: using Python 3.x
Description: A more optimized version of gcd, finds gcd of two numbers
@author: Saptarshi Das
"""
def gcd_opt3(m,n):
    f = min(m,n)
    while f>0:
        if (m%f)==0 and (n%f)==0:
            return(f)
        else:
            i = i-1

    return (f)         #return the highest factor

print("GCD is: ",gcd_opt3(6,12))
