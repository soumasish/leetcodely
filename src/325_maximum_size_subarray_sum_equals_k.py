"""Created by sgoswami on 3/8/17 as part of leetcode"""
"""Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
If there isn't one, return 0 instead."""
import sys

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """


        # index_sum, total = {}, 0,
        # for i, v in enumerate(nums):
        #     total += v
        #     if total not in index_sum:
        #         index_sum[total] = i
        # sum, max_len = 0, -sys.maxsize
        # for i, v in enumerate(nums):
        #     sum += v
        #     if sum == k:
        #         max_len = max(max_len, i+1)
        #     if sum - k in index_sum:
        #         max_len = max(max_len, index_sum[sum-k])
        #
        # return max_len


solution = Solution()
print(solution.maxSubArrayLen([-2, -1, 2, 1], 1))
print(solution.maxSubArrayLen([1, -1, 5, -2, 3], 3))
