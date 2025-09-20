# You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].
# Link : https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
# Approach: Initialize current maximum as first element in the array. For each element in array, update current sum with current element. If current sum is greater than current maximum, update current maximum with current sum's value. If current_sum is less than zero, mark that point as a formation of new sub array by making current sum as zero. 

class Solution:
    def maxSubarraySum(self, arr):

        length = len(arr)
        cur_sum = 0
        cur_max = arr[0]
        
        for i in range(length):
            cur_sum = cur_sum+arr[i]
            cur_max= max(cur_sum, cur_max)

            if cur_sum < 0:
                cur_sum = 0

        return cur_max

soln = Solution()
print(soln.maxSubarraySum([-7,-3,-1,-2,0,-9,8]))