"""Created by sgoswami on 8/13/17."""
"""Given a binary tree, return all root-to-leaf paths."""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        all_paths = []
        curr_path = ''
        self.path_helper(root, curr_path, all_paths)
        return all_paths

    def path_helper(self, root, curr_path, all_paths):
        if root.left == root.right == None:
            curr_path += root.val
            all_paths.apped(curr_path)
            return
        if root.left:
            self.path_helper(root.left, curr_path + str(root.val), all_paths)
        if root.right:
            self.path_helper(root.right, curr_path + str(root.val), all_paths)
