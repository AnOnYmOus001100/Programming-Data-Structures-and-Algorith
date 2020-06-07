"""
ver: using Python 3.x
Description: A more optimized version of gcd(iterativeway2), finds gcd of two numbers(Euclid's Algorithm)
@author: Saptarshi Das
"""
def gcd_ea4(m,n):
    #assume m>=n
    if (m<n):
        (m,n) = (n,m)

    while (m%n) != 0:
        (m,n) = (n,m%n)
    return n
    
print("GCD is: ",gcd_ea4(10,5))
