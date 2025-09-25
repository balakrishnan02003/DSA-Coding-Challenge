# Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].
# Link: https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1
# Approach: The intuition behind this is, the max product elements appear either in prefix or suffix of negative no. Hence we use prefix to operate no. for prefix(1st to last) and suffix(last to first). While processing each element, if current element is zero, that means, there starts a new subarray, hence reset the current multiplied value to 1 so to reset. Current maximum is the maximum value among current prefix,current suffix and previous maximum. To handle an edge case, where array has all negative no.s and zeros, we explicity check for it and return zero in that case; else if not that case, return current maximum after process all elements in the array.
class Solution:
    def maxProduct(self, arr):
        # code here
        cur_max = arr[0]
        prefix = 1
        suffix = 1
        length = len(arr)
        all_negative = True
        has_zero = False
        
        for i in range(0, length):

            if arr[i]==0:
                has_zero = True
            if arr[i]>0:
                all_negative= False
    
            if suffix == 0:
                suffix = 1

            if prefix == 0:
                prefix = 1

            prefix = prefix * arr[i]
            suffix = suffix * arr[length-i-1]

            
            cur_max = max(cur_max, suffix, prefix)
        
        if has_zero is True and all_negative is True:
            return 0

        return cur_max

soln = Solution()
print(soln.maxProduct([-4,0,-1,9,3,4,5,6,0,8,7]))