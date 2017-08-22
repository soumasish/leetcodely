"""Created by sgoswami on 8/11/17."""
"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much 
water it is able to trap after raining."""
import sys

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) == 0:
            return 0
        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]

        left[0] = height[0]
        right[-1] = height[-1]
        left_max = right_max = -sys.maxsize

        for i in range(1, len(height)):
            left_max = max(left_max, height[i-1])
            left[i] = left_max
        height = list(reversed(height))
        right = list(reversed(right))
        for i in range(1, len(height)):
            right_max = max(right_max, height[i-1])
            right[i] = right_max
        height = list(reversed(height))
        right = list(reversed(right))
        total_water = 0
        for i in range(len(height)):
            min_value = min(left[i], right[i])
            water_level = min_value - height[i]
            if water_level > 0:
                total_water += water_level
        return total_water


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))




