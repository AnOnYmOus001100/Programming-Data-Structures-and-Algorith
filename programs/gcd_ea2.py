"""
ver: using Python 3.x
Description: A more optimized version of gcd(iterative way), finds gcd of two numbers(Euclid's Algorithm)
@author: Saptarshi Das
"""
def gcd_ea2(m,n):
    #assume m>=n
    if (m<n):
        (m,n) = (n,m)

    while (m%n) != 0:
            diff = m-n
            (m,n) = (max(n,diff),min(n,diff))
            
    return (n)
    
print("GCD is: ",gcd_ea2(12,9))
