# You are given an integer n. Your task is to reverse the digits, ensuring that the reversed number has no leading zeroes.
# Link: https://www.geeksforgeeks.org/problems/reverse-digit0316/1
# Approach: Extract the last digit using modulo 10. Build reverse no. by multiplying the current reverse no with 10 and adding the extracted digit. Remove the last no by using the floor division. Repeat this process until all no. r processed.
# Difficulty: Basic

class Solution:
    def reverseDigits(self, n):
	    # Code here
        rev = 0
        number = n
        length = len(str(number))
        for i in range(length):
            digit = n%10
            rev = rev*10+digit
            n= n//10
        return rev
    
soln = Solution()
print(soln.reverseDigits(123450))