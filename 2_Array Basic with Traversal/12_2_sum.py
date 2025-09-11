# Given an array arr[] of integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.
# Link: https://www.geeksforgeeks.org/problems/key-pair5616/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
# Approach: Use hashing. Create a set. For number in array, check whether the number target-number is present in that set. If not present, add that number to the set else, return True, mentioning their exist 2 indices such that the sum of their elements is equal to the target. If it didn't returned true even after processing through all elements, then return false.
class Solution:
    def twoSum(self, arr, target):
        # code here
        set1 = set()
        for num in arr:
            check_no = target-num

            if check_no in set1:
                return True
            else:
                set1.add(num)

        else:
            return False

soln = Solution()
print(soln.twoSum([2,4,5,1,2,4],3))
		    