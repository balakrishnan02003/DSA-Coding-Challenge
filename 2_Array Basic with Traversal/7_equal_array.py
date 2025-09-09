# Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.
#Link: https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
# Approach: For each number in the array, use it as a key and increment its count in a dictionary to track how many times it appears.Then, for each element in another array, if the element exists as a key in the dictionary and its count is greater than zero, decrement its count to mark that it has been used once.

class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        hash1 = {}
        for num in a:
            hash1[num]=hash1.get(num,0)+1
            
        for num in b:
            if num in hash1 and hash1[num]>0:
                hash1[num] -= 1
            else:
                return False
        return True
    
soln = Solution()
print(soln.checkEqual([12,14,1,53,1],[1,2,1,54,3]))

    
