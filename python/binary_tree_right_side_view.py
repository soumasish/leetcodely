from collections import defaultdict, deque


class Solution:
    def rightSideView(self, root: Treenode) -> List[int]:
        if not root:
            return []
        levels = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        while len(queue) > 0:
            item = queue.popleft()
            levels[item[1]].append(item[0].val)
            if item[0].left:
                queue.append((item[0].left, item[1] + 1))
            if item[0].right:
                queue.append((item[0].right, item[1] + 1))

        return [val[-1] for val in levels.values()]
