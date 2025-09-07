# You are given a 3-digit number n, Find whether it is an Armstrong number or not.
# Link: https://www.geeksforgeeks.org/problems/armstrong-numbers2727/1
# Approach: Extract the last digit of the number using modulo 10. Then, update the Armstrong value by multiplying the current Armstrong number by 10 and adding the cube of the extracted digit. Finally, remove the last digit from the original number by performing integer division by 10.

class Solution:
    def armstrongNumber (self, n):
        # code here 
        number = n
        arm_no = 0
        for i in range(3):
            digit = number%10
            arm_no = arm_no+digit**3
            number= number//10
        
        if arm_no == n:
            return True
        else:
            return False
        
soln = Solution()
print(soln.armstrongNumber(324))