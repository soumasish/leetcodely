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
        if len(s) == 0 or s == '0':
            return 0

        memo = [None for _ in range(len(s) + 1)]
        memo[0] = 1
        memo[1] = 1
        for i, v in enumerate(s):
            if i == 0:
                continue
            curr = int(s[i])
            previous = int(s[i-1])

            if curr == 0 and previous == 0:
                return 0
            elif curr == 0 and previous * 10 + curr > 26:
                return 0
            elif previous == 0 or previous * 10 + curr > 26:
                memo[i+1] = memo[i]
            elif curr == 0:
                memo[i+1] = memo[i-1]
            else:
                memo[i+1] = memo[i] + memo[i-1]
        print(memo)
        return memo[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.numDecodings('1224'))
