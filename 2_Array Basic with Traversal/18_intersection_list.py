# Given two unsorted integer arrays a[] and b[] each consisting of distinct elements, the task is to return the count of elements in the intersection (or common elements) of the two arrays.
# Link: https://www.geeksforgeeks.org/problems/intersection-of-two-arrays2404/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
# Approach: Use hashing. Perform intersection method in set. To reduce space complexity, I am not storing values in other sets.

class Solution:
    def intersectSize(self,a, b):
        # code here
        #set1=set(a)
        #set2=set(b)
        return len(set(a).intersection(set(b)))
    
soln = Solution()
print(soln.intersectSize([1, 2, 3, 2, 1],[3, 2, 2, 3, 3, 2]))
        
