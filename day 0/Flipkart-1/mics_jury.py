"""
MICS and JURY

The jury consists of M teams of people. Size of each team is given in array teams[]. 
The jury collectively has N mics that must be shared by everyone. 
Find a way to break the teams into N groups such that each group can have its own mic 
and the size of the largest group is minimised. 
"""


#User function Template for python3
import math
class Solution:
    def micsandjury (self, N, M, teams):
        low=1
        high=max(teams)
        result=1
        while(low<=high):
            mid=low+(high-low)//2
            c=0
            for i in teams:
                c=c+math.ceil(i/mid)
            if(c<=N):
                result=mid
                high=mid-1
            else:
                low=mid+1
        return result
        #code here
