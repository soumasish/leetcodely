class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        if n == 0:
            return a
        if n == 1:
            return b
        for i in range(2, n + 1):
            a, b = b, (a + b)
        return b
