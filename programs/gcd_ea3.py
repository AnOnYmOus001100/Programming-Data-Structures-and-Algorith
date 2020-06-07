"""
ver: using Python 3.x
Description: A more optimized version of gcd(recusrsive way2), finds gcd of two numbers(Euclid's Algorithm)
@author: Saptarshi Das
"""
def gcd_ea3(m,n):
    #assume m>=n
    if (m<n):
        (m,n) = (n,m)

    if (m%n) == 0:
        return n
    else:
        return(gcd_ea3(n,m%n))
    
print("GCD is: ",gcd_ea3(100,22))
