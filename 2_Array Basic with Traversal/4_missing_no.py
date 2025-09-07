class Solution:
    def missingNum(self, arr):

        # code here
        n = len(arr)+1
        sum_natural_nos = n*(n+1)//2
        sum = 0
        for i in arr:
            sum +=i
        missing_no = sum_natural_nos - sum
        return missing_no