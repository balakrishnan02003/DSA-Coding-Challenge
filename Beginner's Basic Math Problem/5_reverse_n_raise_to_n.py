# Given a number n, find the value of n raised to the power of its own reverse.
#Link: https://www.geeksforgeeks.org/problems/power-of-numbers-1587115620/1
# Approach:Extract the last digit using modulo 10. Build reverse no. by multiplying the current reverse no with 10 and adding the extracted digit. Remove the last no by using the floor division. Repeat this process until all no. r processed. Then, calculate the orginal number raise to  the reversed no.
# Difficulty: Medium

class Solution:
    def reverseexponentiation(self, n):
        # code here
        number = n
        rev = 0
        length = len(str(number))
        for i in range(length):
            digit = number%10
            rev = rev*10+digit
            number= number//10
            
        return n**rev
soln = Solution()
print(soln.reverseexponentiation(9))
