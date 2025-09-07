# Given a number n, determine whether it is a prime number or not.
#Link: https://www.geeksforgeeks.org/problems/prime-number2314/1
# Approach: Check the divisors of the number up to its square root. This allows you to efficiently find the smallest pair of factors.
class Solution:
    def isPrime(self, n):
        # code here
        if n==1:
            return False
            
        for i in range(2,int((n**0.5))+1):
            if n%i == 0:
                return False
                
        return True
    