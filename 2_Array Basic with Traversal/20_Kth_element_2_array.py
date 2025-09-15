# Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.
# Link: https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
# Approach: Use 2 pointers. Repeat the following till i does k iterations. While indices of 2 arrays aren't out of range, assign value pointed by the index to k_num. If any one of the array reaches the end and other didn't reached the end, place the rest of the elements in k_num.
class Solution:
    def kthElement(self, a, b, k):
        # code here
        a_index = 0
        b_index = 0
        a_length = len(a)
        b_length = len(b)
        for i in range(1,k+1):
            if a_index<=a_length-1 and b_index<=b_length-1:
                if a[a_index]>b[b_index] :
                    k_num=b[b_index]
                    b_index = b_index+1
                elif a[a_index]<=b[b_index] :
                    k_num=a[a_index]
                    a_index = a_index+1
            elif b_index<=b_length-1 and a_index>a_length-1:
                k_num=b[b_index]
                b_index=b_index+1
            elif a_index<=a_length-1 and b_index>b_length-1:
                k_num=a[a_index]
                a_index=a_index+1
            else:
                break
                
        return k_num
                
soln = Solution()
print(soln.kthElement([2, 3, 6, 7, 9],[1, 4, 8, 10],5))