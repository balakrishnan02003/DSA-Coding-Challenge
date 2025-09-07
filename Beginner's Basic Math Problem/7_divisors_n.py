# Given an integer ‘N’, your task is to write a program that returns all the divisors of ‘N’ in ascending order.
#Link: https://www.naukri.com/code360/problems/print-all-divisors-of-a-number_1164188
# Approach: Check the divisors of the number up to its square root. This allows you to efficiently find the smallest pair of factors.

def printDivisors(n):
    # Write your code here

    root = n**0.5
    int_root = int(root)
    lst1 = []
    lst2 = []
    for i in range(1,int_root+1):
        if n%i == 0:
            lst1.append(i)

    length = len(lst1)
    for i in range(0,length):
        val = n//lst1[length-i-1]
        lst2.append(val)
        if lst1[length-1]==lst2[0]:
            lst2.pop(0)
    lst2 = lst1+lst2
    
    return lst2

printDivisors(34)