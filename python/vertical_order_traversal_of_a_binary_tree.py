from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: TreeNode) -> list[list[int]]:
        queue = deque()
        queue.appendleft((root, 0, 0))
        dic = defaultdict(list)
        while len(queue) > 0:
            curr = queue.popleft()
            dic[curr[1]].append((curr[0].val, curr[2]))
            if curr[0].left:
                queue.append((curr[0].left, curr[1] - 1, curr[2] + 1))
            if curr[0].right:
                queue.append((curr[0].right, curr[1] + 1, curr[2] + 1))
        res = []
        for i in sorted(dic.keys()):
            level = sorted([x[1] for x in dic[i]])
            res.append(level)
        return res
