"""Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits.
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9"
 are all invalid."""

from datetime import *


class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        hour, minute = time.split(':')
        digits = set(map(int, [item for item in hour + minute]))

if __name__ == '__main__':
    solution = Solution()
    print(solution.nextClosestTime('19:34'))