"""Created by sgoswami on 8/6/17."""

"""Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are
 overlapped while the others are not.
You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up 
as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree."""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None
        curr_val = 0
        if t1 :
            curr_val += t1.val
        if t2:
            curr_val += t2.val
        node = TreeNode(curr_val)
        node.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        node.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return node



