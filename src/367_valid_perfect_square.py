"""Created by sgoswami on 8/5/17."""
"""Given a positive integer num, write a function which returns True if num is a perfect square else False."""
#TODO: some weird error

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # if num < 1:
        #     return False
        # start, end = 1, num
        # while start <= end:
        #     mid = (end - start)//2
        #     if mid * mid > num:
        #         end = mid - 1
        #     elif mid * mid < num:
        #         start = mid + 1
        #     else:
        #         return True
        #
        # return False

        for i in range(1, num, 2):
            num -= i
            if num == 0:
                return True
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPerfectSquare(121))