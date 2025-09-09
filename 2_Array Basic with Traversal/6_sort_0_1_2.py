# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# Link: https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
# Approach: Use 3 pointers to indicate low, middle and high. store value at arr[mid] and compare whether it is 0 or 1 or 2. If value is 0, increment low and mid and swap(low,mid). If it is 1, increment mid. If the value is 2, swap(mid,high) and decrement high.

class Solution:

    def sort012(self, arr):
        # code here
        low = 0
        mid = 0
        high =len(arr)-1
        while(mid<=high):
            if arr[mid]==0:
                arr[low],arr[mid]=arr[mid],arr[low]
                mid= mid+1
                low = low+1
            elif arr[mid]==1:
                arr[mid]=1
                mid= mid+1
            elif arr[mid]==2:
                arr[mid],arr[high]=arr[high],arr[mid]
                high= high-1
        
        return arr

soln = Solution()
print(soln.sort012([0,1,2,0,1,2]))