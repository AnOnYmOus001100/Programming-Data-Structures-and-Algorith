"""
ver: using Python 3.x
Description: A more optimized version of gcd(recusrsive way), finds gcd of two numbers(Euclid's Algorithm)
@author: Saptarshi Das
"""
def gcd_ea(m,n):
    #assume m>=n
    if (m<n):
        (m,n) = (n,m)

    if (m%n) == 0:
        return n
    else:
        diff = m-n
        return(gcd_ea(max(n,diff),min(n,diff)))
    
print("GCD is: ",gcd_ea(12,9))
