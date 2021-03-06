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

        summation=TreeNode(t1.val+t2.val)
        summation.left = self.mergeTrees(t1.left,t2.left)
        summation.right = self.mergeTrees(t1.right,t2.right)

        return summation
