# Given two positive integers a and b, find GCD of a and b.
# Link: https://www.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1
# Approach: if a = bk + n, then, gcd(a,b) = gcd(b,n) 
class Solution:
    def gcd(self, a, b):
        # code here
        rem = 1
        if a<b:
            dividend = b
            divisor = a
        else:
            dividend = a
            divisor = b
        while (True):
            rem = dividend%divisor
            if rem==0:
                break
            else:
                dividend = divisor
                divisor = rem
                
        return divisor
    
soln = Solution()
print(soln.gcd(12,45))