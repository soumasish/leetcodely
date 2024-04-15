"""Created by sgoswami on 9/4/17."""
"""Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find 
the area of largest rectangle in the histogram."""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        # Initialize stack to store indices, not heights
        stack = [-1]  # Add a sentinel value to avoid empty stack checks
        max_area = 0

        for i in range(len(heights)):
            # Pop from stack while the current height is less than the height at the top of the stack
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1  # Calculate width using indices
                max_area = max(max_area, height * width)

            # Push the current index onto the stack
            stack.append(i)

        # Handle the remaining elements in the stack
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1  # Calculate width using indices
            max_area = max(max_area, height * width)

        return max_area


if __name__ == '__main__':
    solution = Solution()
    print(solution.largestRectangleArea([2, 1, 5, 6, 2, 3]))


