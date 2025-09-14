# Given an array arr[] of integers, determine whether it contains a triplet whose sum equals zero. Return true if such a triplet exists, otherwise, return false.
# Link: https://www.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1
# Approach: 2 pointers approach. At first, sort the array. For each element in the array at the ith index to n-2th index, initialize j=i+1 and k as the last index. If the sum of values at the ith, jth and kth index=0, return true. If the sum is greater than zero, decrement k, else increment j. To handle duplicate values, check if the current value is equal to the previous value which is computed, if yes, move to the next value which has to be computed.
class Solution:
    def findTriplets(self, arr):
        #code here
        arr=sorted(arr)
        length= len(arr)
        i=0
        while(i<length-2):
            if i>0 and arr[i]==arr[i-1]:
                i=i+1
                continue
            j=i+1
            k=length-1
            while(j<k):
                if j>i+1 and arr[j]==arr[j-1]:
                    j=j+1
                    continue
                if k<length-1 and arr[k]==arr[k+1]:
                    k=k-1
                    continue
                tri_sum=arr[i]+arr[j]+arr[k]
                if tri_sum==0:
                    return True
                elif tri_sum<0:
                    j= j+1
                else:
                    k=k-1
       
            i=i+1
        
        return False
                    
soln = Solution()
print(soln.findTriplets([-60,-79, 21, 54, 27, 30, 30]))