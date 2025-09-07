# You are given an integer n. Your task is to determine whether it is a palindrome.
#Link: https://www.geeksforgeeks.org/problems/palindrome0746/1
#Approach: Extract the last digit of the number using modulo 10. Then, update the reverse number by multiplying the current reverse number by 10 and adding the extracted digit. Finally, remove the last digit from the original number by performing integer division by 10.

class Solution:
    def isPalindrome(self, n):
		# code here
        number = n
        length = len(str(n))
        rev = 0
        for i in range(length):
            digit = number%10
            rev = rev*10+digit
            number = number//10
		  
        if rev == n:
            return True
        else:
            return False
        
soln = Solution()
print(soln.isPalindrome(4343))
