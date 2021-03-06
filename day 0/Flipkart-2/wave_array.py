"""
Wave Array

Given a sorted array arr[] of distinct integers. Modify the array to look like a wave. In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....
Note: The converted array must be the lexicographically smallest wave array.


Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 2 1 4 3 5

#User function Template for python3

class Solution:
    def convertToWave(self, arr, N):
        if(len(arr)<2):
            return arr
        arr.sort()
        for i in range(len(arr)-1):
            if(i%2==0 and arr[i]<arr[i+1]):
                m=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=m
        return arr
        # code here
