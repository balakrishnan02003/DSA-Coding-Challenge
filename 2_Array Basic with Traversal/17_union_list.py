# You are given two arrays a[] and b[], return the Union of both the arrays in any order.

# The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.

# Note: Elements of a[] and b[] are not necessarily distinct.
# Note that, You can return the Union in any order but the driver code will print the result in sorted order only.
# Link: https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1
# Approach: Use hashing. Convert list to set and use inbuild union operation in set and return it.

class Solution:    
    def findUnion(self, a, b):
        # code here
        set1 = set(a)
        set2 = set(b)
        
        return set1.union(set2)
        
soln = Solution()
print(soln.findUnion([1, 2, 1, 1, 2],[2, 2, 1, 2, 1] ))