#Given an array of integers arr[]. You have to find the Inversion Count of the array. 
#Note : Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].
#Link: https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1
# Approach: It's core idea is based on merge sort. Consider 2 sorted arrays, a and b. If a[i] is greater than b[j], which means we can form a pair (a[i],b[j]). Since a is sorted, it is obvious that remaining elements in a can also form pair with b[j]. So, to make sorted sub array, we use the merge sort algorithm and sort using merge() and carry inversion count using mid-i+1
class Solution:
    def inversionCount(self, arr):
        # Code Here
        end = len(arr)-1
        count=0
        def mergesort(arr,start,end):
            nonlocal count
            if start<end:
                mid = (start+end)//2
                mergesort(arr,start,mid)
                mergesort(arr,mid+1,end)
                merge(arr,start,mid,end)
            return count
        
        def merge(arr,start,mid,end):
            nonlocal count
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
                    count+= mid-i+1
            
            while i<=mid:
                sorted_array.append(arr[i])
                i=i+1
            while j<=end:
                sorted_array.append(arr[j])
                j=j+1
            
            arr[start:end+1]=sorted_array
            
            
            
        count = mergesort(arr,0,end)
        return count
    
soln = Solution()
print(soln.inversionCount([2, 4, 1, 3, 5]))
