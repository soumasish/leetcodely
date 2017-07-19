"""Created by sgoswami on 7/9/17."""
"""A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.
For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
The number of ways decoding "12" is 2."""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == '' or s == '0':
            return 0
        elif len(s) == 1:
            return 1
        count, i = 0, 0
        while i < len(s):
            single = int(s[i:i+1])
            double = int(s[i:i+2])
            if single != 0 and 0 < double <= 26:
                count += 2
            if single != 0 or 0 < double <= 26:
                count += 1
            i += 1
        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.numDecodings('12'))
