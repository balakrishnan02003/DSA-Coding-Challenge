# Given an array arr, count the number of distinct triplets (a, b, c) such that:
# a + b = c
# Each triplet is counted only once, regardless of the order of a and b.
# Link: https://www.geeksforgeeks.org/problems/count-the-triplets4615/1
# Approach: Sort the array. let i points to the last index. high points to  i-1th index and low points to first index. If sum of elements at the low and high index is equal to element at the ith index, increment count, if value is lower than element at i, then increment low else decrement high. Repeat this inner loop till low<high. Then, decrement i by 1. Repeat this till i>1.

class Solution:
    def countTriplet(self, arr):
        # code here
        arr = sorted(arr)
        count = 0
        i = len(arr) - 1
        while(i > 1):
            low = 0
            high = i - 1
            while(low < high):
                if arr[i] == arr[low] + arr[high]:
                    count = count + 1
                    low = low + 1
                    high = high - 1
                elif arr[i] > arr[low] + arr[high]:
                    low = low + 1
                else:
                    high = high - 1
            i = i - 1
        return count

soln = Solution()
print(soln.countTriplet([1, 5, 3, 2]))
		    
	           
	            