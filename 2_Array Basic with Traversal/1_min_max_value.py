class Solution:
    def get_min_max(self, arr):
        
        length = len(arr)
        sorted_array = sorted(arr)
        return sorted_array[0],sorted_array[length-1]