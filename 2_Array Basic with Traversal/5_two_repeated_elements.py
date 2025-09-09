# You are given an integer array arr of size n+2. All elements of the array are in the range from 1 to n. Also, all elements occur once except two numbers which occur twice. Find the two repeating numbers.
# Link: https://www.geeksforgeeks.org/problems/two-repeated-elements-1587115621/1
# Approach: Since all numbers are in the range from 1 to n, we can use the array itself to track occurrences. As we iterate through the array, for each element val, we access the index abs(val) and negate the value at that index to mark it as visited. If any  duplicate element got encountered, the value becomes positive as it is again negated, thus we mark as duplicated. This way, at the end of scanning of array, we can find the duplicate elements in that array.

class Solution:
    def twoRepeated(self, arr):
        # code here
        lst1 = []
        for i in range(0,len(arr)):
            val = abs(arr[i])
            arr[val]= -arr[val]
            
            if arr[val]>0:
                lst1.append(val)
        
        return lst1

soln = Solution()
print(soln.twoRepeated([1,2,1,3,4,4]))
