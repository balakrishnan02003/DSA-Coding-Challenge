# Given a positive integer n, count the number of digits in n that divide n evenly (i.e., without leaving a remainder). Return the total number of such digits.
# Link: https://www.geeksforgeeks.org/problems/count-digits5716/1
# Approach: Get the last digit using modulo 10. If the digit is non-zero (since division by zero is undefined) and divides the orginal number evenly, then increment count. Then, perform floor division to remove the last digit. Repeat this step until the orginal number becomes zero.
#Difficulty: Easy

class Solution:
    def evenlyDivides(self, n):
        # code here
        number = n
        length = len(str(n))
        count = 0
        for i in range(length):
            digit = number%10
            if digit != 0:
                if n%digit == 0:
                    count = count+1
            number = number//10
        return count
    
soln = Solution()
print(soln.evenlyDivides(23434))