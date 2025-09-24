class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        for i in range(len(intervals)-1):
            if intervals[i[1]]> intervals[i+1[0]]:
                arr = [intervals[i[0]],intervals[i+1[1]]]
                intervals.pop(i)
                intervals.pop(i+1)
                intervals.insert(i,arr)
        
        return intervals