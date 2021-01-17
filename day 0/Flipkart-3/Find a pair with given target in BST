"""
Find a pair with given target in BST 

Given a Binary Search Tree and a target sum. Check whether there is a pair of Nodes in the BST with value summing up to the target sum. 
Example 1:

Input:
        2
      /   \
     1     3
sum = 5
Output: 1
"""


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
def isPairPresent(root, target):
    if(root is None):
        return False
    queue=[]
    queue.append(root)
    l=[]
    while(len(queue)!=0):
        l.append(queue[0].data)
        node=queue.pop(0)
        if(node.left is not None):
            queue.append(node.left)
        if(node.right is not None):
            queue.append(node.right)
    i=0
    l=list(set(l))
    for x in l:
        if((target-x) in l):
            i=1
            break
    if(i==1):
        return 1
    else:
        return 0
        
    
    # code here
