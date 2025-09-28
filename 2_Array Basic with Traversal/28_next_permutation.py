# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
#Link : https://leetcode.com/problems/next-permutation/
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        sorted_subarray = []
        flag = 0

        for i in range(length-1,0,-1):
            if nums[i]>nums[i-1]:
                idx = i-1
                flag = 1
                break
        
        if flag==1:
            for i in range(length-1,i-1,-1):
                if nums[idx] < nums[i]:
                    nums[i],nums[idx]=nums[idx],nums[i]
                    break
        
            sorted_subarray= sorted(nums[idx+1::])
            nums[idx+1::]=sorted_subarray
  
        else:
            nums[:] = nums[::-1]    
      
    
soln = Solution()
arr = [3,2,1]
soln.nextPermutation(arr)
print(arr)