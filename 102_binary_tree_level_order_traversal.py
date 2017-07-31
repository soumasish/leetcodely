"""Created by sgoswami on 7/19/17."""
"""Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right,
 level by level)."""
import collections

# Definition for a binary tree node.
class BST:
    def __init__(self):
        self.root = None

    def insert(self, item):
        self.root = self.insert_helper(self.root, item)
        return self.root

    def insert_helper(self, root, item):
        if root is None:
            root = TreeNode(item)
            return root
        if item < root.val:
            root.left = self.insert_helper(root.left, item)
        else:
            root.right = self.insert_helper(root.right, item)
        return root

    def inorder(self):
        self.inorder_helper(self.root)

    def inorder_helper(self, root):
        if root is None:
            return
        self.inorder_helper(root.left)
        print(root.val, end=', ')
        self.inorder_helper(root.right)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res, curr_list = [], []
        queue = collections.deque()
        queue.appendleft(root)
        queue.appendleft('#')
        while len(queue) > 0:
            curr_node = queue.pop()
            if curr_node == '#':
                if len(queue) > 0:
                    queue.appendleft('#')
                res.append(curr_list)
                curr_list = []
                continue
            else:
                curr_list.append(curr_node.val)
            if curr_node.left:
                queue.appendleft(curr_node.left)
            if curr_node.right:
                queue.appendleft(curr_node.right)
        return res

if __name__ == '__main__':
    bst = BST()
    bst.insert(3)
    bst.insert(9)
    bst.insert(15)
    bst.insert(7)
    #bst.inorder()
    solution = Solution()
    print(solution.levelOrder(bst.root))