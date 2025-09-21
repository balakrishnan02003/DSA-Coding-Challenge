# You are given an integer array arr[]. You need to find the subarray whose sum is maximum (containing at least one element) in the array arr[].
# Approach: Same as Kadane's algorithm. Here, use 3 pointers: temp_start,start and end and initilaize them to zero. If the current sum becomes zero, point temp_start to the next element in the array. If the current sum is greater than current maximum, update start with temp_start and end with i.
class Solution:    
    def maxSubarray(self, arr):

        length = len(arr)
        cur_sum = 0
        cur_max = arr[0]
        temp_start = 0
        start = 0
        end = 0
        
        for i in range(length):
            cur_sum = cur_sum+arr[i]

            if cur_sum > cur_max:
                start = temp_start
                end = i

            cur_max= max(cur_sum, cur_max)

            if cur_sum < 0:
                cur_sum = 0
                temp_start = i+1

        return cur_max, arr[start:end+1]

soln = Solution()
print(soln.maxSubarray([-8,-2,-3,-1,-3]))