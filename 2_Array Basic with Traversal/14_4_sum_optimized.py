# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# Link: https://leetcode.com/problems/4sum/
# Approach: For each element i in the array, select j as i+1, and k as j+1 and l as length of array-1. compute the sum at these 4 index. If the sum is equal to the target value, add to the list, if it is less than target value, increment j else decrement k. Repeat it till j becomes length of array -2. Repeat this till i becomes length of array - 3.
# Y is this efficient than complement method soln: 
# 1,In this soln, there is no set operation. Even though set operation takes only O(1), looping through all combination increases the cost. 
# 2,Here the space complexity is O(1). For previous soln, the space complexity was O(n) due to extra space for the set.
# 3, This soln handled duplication at the earlier stage itself(at traversal); but the previous soln, duplication was handled at the end, which increases the compulation cost.
# -> In leetocode, it took only 891ms to run this soln, but took 1044ms to run the previous one.

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res_lst = []
        nums = sorted(nums)

        i=0 # i Initilaize
        length = len(nums)
        while(i<length-3): # outer loop
            if i>0 and nums[i]==nums[i-1]: # Duplicate-i 
                i=i+1
                continue      
            
            j=i+1 # j Initilalize
            while(j<length-2): # inner loop
                if j>i+1 and nums[j]==nums[j-1]: # Duplicate-j
                    j=j+1
                    continue

                k=j+1 # k Initialize
                l=length-1 # l initialize
                while(k<l): # inner-most loop
                    if k>j+1 and nums[k]==nums[k-1]: # Duplicate-k
                        k=k+1
                        continue

                    if l<length-1 and nums[l]==nums[l+1]:# Duplicate-l
                        l=l-1
                        continue

                    quad_sum=nums[i]+nums[j]+nums[k]+nums[l]

                    if quad_sum==target:
                        res_lst.append([nums[i],nums[j],nums[k],nums[l]])
                        print([nums[i],nums[j],nums[k],nums[l]])
                        k=k+1
                        l=l-1

                    elif quad_sum<target:
                        k=k+1

                    else:
                        l=l-1

                j=j+1 # j increment

            i=i+1 # i increment
        
        return res_lst
    
soln = Solution()
print(soln.fourSum([-2,-1,-1,1,1,2,2],0))


                        
