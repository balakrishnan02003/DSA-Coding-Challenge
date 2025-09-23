

class Solution:
    def inversionCount(self, arr):
        # Code Here
        end = len(arr)-1
        count=0
        def mergesort(arr,start,end):
            nonlocal count
            if start<end:
                mid = (start+end)//2
                count += mergesort(arr,start,mid)
                count += mergesort(arr,mid+1,end)
                count += merge(arr,start,mid,end)
            return count
        
        def merge(arr,start,mid,end):
            sorted_array = []
            i=start
            j=mid+1
            
            while i<=mid and j<=end:
                if arr[i]<=arr[j]:
                    sorted_array.append(arr[i])
                    i=i+1
                else:
                    sorted_array.append(arr[j])
                    j=j+1
                    count += mid-i+1
            
            while i<=mid:
                sorted_array.append(arr[i])
                i=i+1
            while j<=end:
                sorted_array.append(arr[j])
                j=j+1
            
            arr[start:end+1]=sorted_array
            return count
            
            
        count = mergesort(arr,0,end)
        return count
    
soln = Solution()
print(soln.inversionCount([2, 4, 1, 3, 5]))