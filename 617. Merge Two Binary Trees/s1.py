#617. Merge Two Binary Trees
#https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """      

        summation=TreeNode(0)

        if (t1 is None) and (t2 is None):
            return None
        if (t1 is None):
            return t2
        if (t2 is None):
            return t1

        if t1.val>0 or t2.val>0:

            summation=TreeNode(t1.val+t2.val)

            #node_1 = t1.left if (t1.left is not None) else None
            #node_2 = t2.left if (t2.left is not None) else None
            summation.left = self.mergeTrees(t1.left,t2.left)
            #if summation.left.val == 0:
             #   summation.left = None 

            #node_1 = t1.right if (t1.right is not None) else TreeNode(0)
            #node_2 = t2.right if (t2.right is not None) else TreeNode(0)
            summation.right = self.mergeTrees(t1.right,t2.right)
            #if summation.right.val == 0:
                #summation.right = None 

        return summation
