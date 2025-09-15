# You are given a sorted array arr[] containing positive integers. Your task is to remove all duplicate elements from this array such that each element appears only once. Return an array containing these distinct elements in the same order as they appeared.
# Link: https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
# Approach: Use 2 pointers approach. Take first index as i and 2nd index as j. While j less than length of the array, check if the jth element is same as j-1th element, if true, increment j, else, increment i, then replace the value at ith index with value pointed by j then increment j. Finally, return the array from 0th to ith index.    
class Solution:
    def removeDuplicates(self, arr):
        # code here 
        length = len(arr)
        i=0
        j=i+1
        while(j<length):
            if arr[j-1]==arr[j]:
                j=j+1
            else:
                i=i+1
                arr[i]=arr[j]
                j=j+1
                
        return arr[0:i+1]