# You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].
# Link : https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
# Approach : Initialize maxi as the first value in the array. If maxi and current_element are negative no.s, check whether the current element is greater than maxi, if true, then update maxi with current element. Update c_sum by adding with with current element in the array. If c_sum is less than 0, update c_sum as 0. If maxi is postive and c_sum is greater than 0 or if arr[i] is zero and current value is greater than mazi, then update maxi with c_sum
class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        c_sum = 0
        maxi = arr[0]
        length = len(arr)
        
        for i in range(length):
            
            if maxi < 0 and arr[i] < 0:
                if maxi < arr[i]:
                    maxi = arr[i]
                
            c_sum = c_sum+arr[i]
            if c_sum <0:
                c_sum=0
         
            if (maxi < c_sum and c_sum>0) or (arr[i]==0 and arr[i]>maxi):
                maxi = c_sum
                
        return maxi

soln = Solution()
print(soln.maxSubarraySum([2, 3, -8, 7, -1, 2, 3]))