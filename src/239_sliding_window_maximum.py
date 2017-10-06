"""Created by sgoswami on 10/4/17."""
"""Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position."""
import sys

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        results = []
        curr_max_left, curr_max_right = -sys.maxsize, -sys.maxsize
        max_left = []
        max_right = []
        for i in range(len(nums)):
            j = -i -1
            curr_max_left = max(curr_max_left, nums[i])
            max_left.append(curr_max_left)
            curr_max_right = max(curr_max_right, nums[j])
            max_right.append(curr_max_right)

        for i in range(len(nums) - k):
            curr_max = max(curr_max_left[i], curr_max_right[i + k])
            results.append(curr_max)
        return results

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))


