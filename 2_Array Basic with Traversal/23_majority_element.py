# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Link: https://leetcode.com/problems/majority-element/description/
# Approach; Use hashing. For each element, enter that element as key and it's occurrence as it's value. Update occurence each time the value appear int the array. If the value of the occurence is greater than the length//2, return it's corresponding key.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1 = {}
        length = len(nums)
        for num in nums:
            dict1[num]=dict1.get(num,0)+1

            if dict1[num]== (length+1)//2:
                return num
        
soln = Solution()
print(soln.majorityElement([0,0,1,2,2,1,0,0,0,0]))