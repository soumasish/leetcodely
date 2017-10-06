"""Created by sgoswami on 9/4/17."""
"""Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find 
the area of largest rectangle in the histogram."""

#TODO: Still not completely correct
class stack:
    def __init__(self):
        self.store = []
        self.size = 0

    def push(self, item):
        self.store.append(item)
        self.size += 1

    def peek(self):
        if self.size == 0:
            return KeyError('Peeking an empty stack')
        return self.store[-1]

    def pop(self):
        if self.size == 0:
            return KeyError('Popping an empty stack')
        self.size -= 1
        return self.store.pop()

    def is_empty(self):
        return self.size == 0


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights or len(heights) == 0:
            return 0
        stack = []
        i, area = 0, -1
        while i < len(heights):
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                if len(stack) == 0:
                    curr_area = heights[top] * i
                else:
                    curr_area = heights[top] * (i - stack[-1] - 1)
                area = max(area, curr_area)

        while len(stack) > 0:
            top = stack.pop()
            if len(stack) == 0:
                curr_area = heights[top] * i
            else:
                curr_area = heights[top] * (i - stack[-1] -1)
            area = max(area, curr_area)
        return area

if __name__ == '__main__':
    solution = Solution()
    print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))


