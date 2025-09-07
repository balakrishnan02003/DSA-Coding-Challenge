#Given a positive integer n, find the square root of n. If n is not a perfect square, then return the floor value.
#Link: https://www.geeksforgeeks.org/problems/square-root/1
# Approach: Use int() on the sqrt.
class Solution:
    def floorSqrt(self, n): 
        # code here
        return int(n**0.5)
    
soln = Solution()
print(soln.floorSqrt(43))