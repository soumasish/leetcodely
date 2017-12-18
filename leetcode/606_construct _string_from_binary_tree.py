"""Created by sgoswami on 8/7/17."""
"""You need to construct a string consists of parenthesis and integers from a binary tree with the preorder 
traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis 
pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree."""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        tree_list = []
        self.helper()

    def helper(self):
        pass