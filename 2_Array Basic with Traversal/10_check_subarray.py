# Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].
# Link: https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1
# Approach: Create dictionary for the elements in array a. Key is the element of the array and value is the occurance of each element. Check whether the element in b present in b by checking with the key and occurence is greater than zero. If it is decrease the value of key.

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        hash1 ={}
        for num in a:
            hash1[num]= hash1.get(num,0)+1
            
        for num in b:
            if num not in hash1 or hash1[num]==0:
                return False
            else:
                hash1[num]-=1
        
        return True