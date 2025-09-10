# Given an array 'arr' with 'n' elements, the task is to rotate the array to the left by 'k' steps, where 'k' is non-negative.
# Link: https://www.codingninjas.com/studio/problems/rotate-array_1230543
# Approach: Since it is left rotated, store k elements from the starting index and store it in a list, so that value won't lose due to overwritten. Then, move the element in ith index to the i-kth index till i reaches the last index. Then, copy the list values from length-kth index.

def rotateArray(arr: list, k: int) -> list:
    # Write your code here.
    length_array= len(arr)
    k = k%length_array
    lst1=[]
    for i in range(k):
        lst1.append(arr[i])

    
    for i in range(k,length_array):
        arr[i-k]=arr[i]

    j=length_array-k
    for num in lst1:
        arr[j]=num
        j = j+1
    
    return arr

print(rotateArray([1,2,3,4,5,6,7],4))