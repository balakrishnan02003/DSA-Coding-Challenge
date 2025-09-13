# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# Link: https://leetcode.com/problems/4sum/
# Approach: Extended version of 3_sum. For each element in the array at the ith index, calculate the difference b/w that element and the target value, then apply 3-sum logic. Repeat it till i reaches to n-2.
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        lst1 = []
        for i in range(0,n-2):
            complement1 = target-nums[i]
            for j in range(i+1,n-1):
                set1 = set()
                complement2 = complement1-nums[j]
                for k in range(j+1,n):
                    complement3 = complement2-nums[k]
                    if complement3 in set1 and [nums[i],nums[j],complement3,nums[k]] not in lst1:
                        lst1.append([nums[i],nums[j],complement3,nums[k]])
                        #print([nums[i],nums[j],complement3,nums[k]]) # For debugging!
                    else:
                        set1.add(nums[k])

        return lst1
    
soln = Solution()
print(soln.fourSum([1, 1, 2, 2, 2, 2, 3, 3],8))




