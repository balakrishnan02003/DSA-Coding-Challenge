# Given an array arr[] with non-negative integers representing the height of blocks. If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
# Link: https://www.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
# Approach: The amount of water unit that can be hold in a particular index is 
# min(largest_left[i],largest_right[i])-a[i]; where largest_left[i] is the maximum height from the 0th to the ith index, and largest_right[i] be the maximum height from the ith to the last index in the array.

# Better soln: It can be solved by creating 2 arrays, one contains the value of largest from the left upto current index and another array contains the largest value from upto current index. The water unit holds in the particular index is the min(largest_left,largest_right - a[i]); if value is negative or 0, then water hold in that index is 0; else the value is the water trapped b/w at that index. Here, space complexity is O(2*n) and time complexity is O(n)+O(n)+O(n)-> O(n)

# Optimal soln: This is implemented. Here, left_pointer points to the first index and right_pointer points to the last index. First check whether a[left pointer]<=a[right_pointer], if true, it means there exist a building in the right whose height is more than or equal to the left building which is currently pointed. 
# Hence, min(largest_left[i],largest_right[i]) is always gonna be largest_left[i]. If arr[left_pointer] is greater than current_left_max, left_max with arr[l] and move to next index, In this case, amount of water is not gonna change, as it can't hold the water. else, water=water+left_max-a[l]. It works the other way around when a[left_pointer]>a[right_pointer]. Here, space complexity is O(1) and time complexity is O(n).
class Solution:
    def maxWater(self, arr):
        # code here
        l = 0
        r = len(arr)-1
        left_max=0
        right_max=0
        water=0
        
        while(l<r):
            if arr[l]<=arr[r]:
                if arr[l]>left_max:
                    left_max=arr[l]
                    l=l+1
                else:
                    water=water+left_max-arr[l]
                    l=l+1
            else:
                if arr[r]>right_max:
                    right_max=arr[r]
                    r=r-1
                else:
                    water=water+right_max-arr[r]
                    r=r-1
        
        return water
    
soln = Solution()
print(soln.maxWater([3, 0, 1, 0, 4, 0 ,2]))