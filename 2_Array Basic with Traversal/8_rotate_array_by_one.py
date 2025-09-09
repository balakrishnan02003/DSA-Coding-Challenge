# Given an array arr, rotate the array by one position in clockwise direction.
# Link: https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
# Approach: Store the last element(coz it's clockwise rotated, the value gets overwritten thus, we lost the value) then store the value in len-ith index value with len-1-ith index through out the array and store the value of the last value on the 0th index to complete the rotation.

class Solution:
    def rotate(self, arr):
        length = len(arr)
        a = arr[length-1]
        for i in range(1,length):
            arr[length-i]= arr[length-1-i]
        
        arr[0]=a
        return arr
    
soln = Solution()
print(soln.rotate([12,13,18,1,4]))
