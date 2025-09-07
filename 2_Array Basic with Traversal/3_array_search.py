class Solution:
    def search(self, arr, x):
        # code here
        for i in range(len(arr)):
            if x == arr[i]:
                return i
        else:
            return -1
        