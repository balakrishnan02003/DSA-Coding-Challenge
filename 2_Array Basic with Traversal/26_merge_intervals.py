# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# Link: https://leetcode.com/problems/merge-intervals/description/
# Approach: Sort the elements in the list. If the value of element's 1st index is higher than or equal to the value of element's 0th index of next element, then remove those elements and add value to the array at the current position, where value is element in the 0th index at the current position and maximum among element at 1st index in ith or i+1th index. 
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        i=0
        while i<len(intervals)-1:
            if intervals[i][1]>= intervals[i+1][0]:
                arr = [intervals[i][0],max(intervals[i+1][1],intervals[i][1])]
                intervals.pop(i)
                intervals.pop(i) # Since the ith element is already popped, the i+1th element becomes ith element.
                intervals.insert(i,arr)
                
            else:
                i=i+1
        
        return intervals     

soln = Solution()
print(soln.merge([[1,3],[2,6],[8,10],[15,18]]))
