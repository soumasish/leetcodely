"""Created by sgoswami on 8/13/17."""
"""Given a binary tree, return all root-to-leaf paths."""

from leetcode.data_types.binary_search_tree import BinarySearchTree

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

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(12)
    bst.insert(9)
    bst.insert(13)
    bst.insert(4)
    bst.insert(10)
    bst.insert(17)
    solution = Solution()
    print(solution.binaryTreePaths(bst.root))

