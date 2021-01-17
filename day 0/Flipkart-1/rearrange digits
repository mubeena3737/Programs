"""
Rearrange the Digits

Given a number N, find the smallest number which can be obtained by rearranging the digits of N. The generated number should not have any leading zeroes.

Example 1:

Input: N = 846903
Output:304689
""""


#User function Template for python3


class Solution:
    def smallestnum (self,ans):
        for i,n in enumerate(ans):
            if n!=0:
                temp=ans.delete(i)
                break
        return str(temp)+''.join(ans)
        # code here 
