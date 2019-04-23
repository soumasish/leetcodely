"""Created by sgoswami on 8/30/17."""
"""Implement pow(x, n)."""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
