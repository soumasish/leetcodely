"""Created by sgoswami on 3/8/17 as part of leetcode"""
"""Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
If there isn't one, return 0 instead."""


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_len, curr_total = 0,0
        for i, v in enumerate(nums):
            curr_total = v
            if curr_total == k:
                max_len = max(max_len, 1)
            for j, w in enumerate(nums):
                if j > i:
                    curr_total += w
                    if curr_total == k:
                        max_len = max(max_len, (j - i)+1)
        return max_len

solution = Solution()
print(solution.maxSubArrayLen([-2, -1, 2, 1], 1))
print(solution.maxSubArrayLen([1, -1, 5, -2, 3], 3))
