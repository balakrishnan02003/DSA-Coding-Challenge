# Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.
# Link: https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
# Approach: Use hashing. Use dictionary, so that, it holds the cumulative sum at it's key and it's postion in value. So, create the dictionary, which already have 0 at key and -1 at it's postion. For each element in the array, add the key value pair to the dictionary, if the cumulative sum isn't already present in the key. If the difference b/w the cumulative sum and the k is present in the dictionary key, that means, there exist a sub-array with the current value as it's last index which sum to k. Find it's length of that sub array by finding the difference b/w current i and the value of complement key. If it is greater than the current longest_length found, then update the value by the length of the current sub array length. 
class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        longest_length = 0
        length= len(arr)
        dict1 = {0:-1}
        sum = 0
        for i in range(length):
            sum = sum+arr[i]
            complement = sum-k
            
            if sum not in dict1:
                dict1[sum]=i
            
            if complement in dict1:
                sub_array_length = i-dict1[complement]
                
                if sub_array_length > longest_length:
                    longest_length=sub_array_length
                
        return longest_length
            
                      
soln = Solution()
print(soln.longestSubarray([10,5,2,7,1,-10],15))