class Solution:
    def thirdLargest(self,arr):
        # code here
        if len(arr)<=2:
            return -1
        else:
            for i in range(3):
                for j in range(len(arr)-1-i):
                    if arr[j]>arr[j+1]:
                        arr[j],arr[j+1]=arr[j+1],arr[j]
            
            return arr[len(arr)-3]