# Given a number n, check if the number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number.
# Link:https://www.geeksforgeeks.org/problems/perfect-numbers3207/1
# Approach: The smallest pair of multiplier will come inb/w 1 and the root of the number. Then find the largest no. of that pair.
class Solution:
    def isPerfect(self, n):
        # code here 
        lst1 = []
        lst2 = []
        range_max = int(n**0.5)+1
        for i in range(1,range_max):
            if n%i==0:
                lst1.append(i)
        
        for i in lst1:
            val = n//i
            if val == lst1[len(lst1)-1]:
                continue
            lst2.append(val)
            
        lst2 = lst1+lst2
        
        if sum(lst2)-n == n:
            return True
        else:
            return False
    
soln = Solution()
print(soln.isPerfect(43))