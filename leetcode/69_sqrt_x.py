"""Implement int sqrt(int x).
Compute and return the square root of x."""

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        low, high = 1, x
        while low +1 < high:
            mid = low + (high - low)//2
            if mid * mid < x:
                low = mid
            elif mid * mid > x:
                high = mid
            else:
                return mid
        return low

if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt(5))