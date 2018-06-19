"""Created by sgoswami on 7/19/17."""
"""Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right,
 level by level)."""
from collections import deque
from .data_types.binary_search_tree import BinarySearchTree


# Definition for a binary tree node.

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, curr_list = [], []
        queue = deque()
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
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(9)
    bst.insert(15)
    bst.insert(7)
    solution = Solution()
    print(solution.levelOrder(bst.root))