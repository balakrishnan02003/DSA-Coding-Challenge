# You are given an array arr[] containing positive integers. The elements in the array arr[] range from  1 to n (where n is the size of the array), and some numbers may be repeated or absent. Your have to count the frequency of all numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).
# Link: https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1
# Approach: Create a array of same the size of input array to make the frequency. For num in the input array, increment the value of frequency array at the index num-1.

class Solution:
    def frequencyCount(self, arr):
        #  code here
        array_length = len(arr)
        freq_array = [0]*(array_length)
        for num in arr:
            freq_array[num-1]+=1
            
        return freq_array
    
soln = Solution()
print(soln.frequencyCount([2,1,2,4,2,3]))