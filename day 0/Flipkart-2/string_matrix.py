"""
String Matrix

A[][] is a (R x C) boolean matrix  such that each of its element is either 0 or 1. Each row of the matrix is sorted. Find the index of the row which has the maximum number of ones. If there are multiple such rows then return the smallest index.
An array B[] of size R is used to construct matrix A such that B[i] denotes the number of zeroes in the ith row.


Example 1: 

Input:
R=3, C=3
B[]={1, 0, 2} 

Output: 1
"""


#User function Template for python3

class Solution:
    # do not edit this function
    # use it to get the value of A[i][j]
    def get(self, i, j):
      return a.get(i,j)
      
    def solve(self, R, C):
        k=0
        r=0
        l=C-1
        for i in range(R):
            while(l>=0 and a.get(i,l)):
                l=l-1
                k=i
        return k
        # code here
