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
    #     all_paths = []
    #     curr_path = ''
    #     self.path_helper(root, curr_path, all_paths)
    #     return all_paths
    #
    # def path_helper(self, root, curr_path, all_paths):
    #     if not root.left and not root.right:
    #         curr_path += root.val
    #         all_paths.append(curr_path)
    #         return
    #     if root.left:
    #         self.path_helper(root.left, curr_path + str(root.val), all_paths)
    #     if root.right:
    #         self.path_helper(root.right, curr_path + str(root.val), all_paths)
        all_paths = []
        curr_path = ''
        self.helper(root, all_paths, curr_path)
        return all_paths

    def helper(self, root, all_paths, curr_path):
        if not root.left and not root.right:
            curr_path += str(root.val)
            all_paths.append(curr_path)
            return
        curr_path += str(root.val)
        curr_path += '->'
        if root.left:
            self.helper(root.left, all_paths, curr_path)
        if root.right:
            self.helper(root.right, all_paths, curr_path)




class StringBuilder():
    def __init__(self):
        self.store = []

    def append(self, item):
        self.store.append(item)

    def build(self):
        return ''.join(self.store)