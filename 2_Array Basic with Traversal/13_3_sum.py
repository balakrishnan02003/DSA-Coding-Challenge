# Given an array arr[] and an integer target, determine if there exists a triplet in the array whose sum equals the given target.
# Link: https://www.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
# Approach: This is an extended version of 2-sum problem. Fro each element at the index i in array, calculate the difference b/w target value and the element at the ith index, then apply 2 sum problem logic. That is, for remaining elements in the array, find the difference b/w the previously computed value and the current element. check if the currently computed value exist in the set. If yes, then return true, else, store the current element in the list, repeat this till traversal happens to the end to the list. Then reset the set. Continue this until i becomes n-1.
class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        
        n = len(arr)
        for i in range(0,n-1):
            set1 = set()
            complement1 = target-arr[i]
            for j in range(i+1,n):
                complement2 = complement1-arr[j]
                if complement2 in set1:
                    return True
                else:
                    set1.add(arr[j])
                
        else:
            return False
        
soln = Solution()
print(soln.hasTripletSum([1, 4, 45, 6, 10, 8],13))