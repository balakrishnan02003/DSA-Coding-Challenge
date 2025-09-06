# Problem: Check if a number is even
# link: https://practice.geeksforgeeks.org/problems/odd-or-even3618/1
# Approach : check if number is divisible by 2 using modulus operator.
# Difficulty: Easy

class Solution:
    def isEven (self, n):
        # code here 
        if n%2 ==0:
            return True
        else:
            return False

soln = Solution()
print(soln.isEven(15))
