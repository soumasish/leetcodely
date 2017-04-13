"""Created by sgoswami on 3/8/17 as part of leetcode"""
"""Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
If there isn't one, return 0 instead."""
from collections import deque


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total, curr_len, max_len = 0, 0, 0
        trigger = False
        q = deque()
        for item in nums:
            q.append(item)
            if trigger:
                element = q.popleft()
                total -= element
                total += item
            else:
                total += item
                curr_len += 1
            if total == k:
                trigger = True
                max_len = max(max_len, curr_len)
        if not trigger:
            return 0
        else:
            return max_len
