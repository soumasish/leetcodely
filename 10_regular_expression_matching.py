"""Created by sgoswami on 7/9/17."""
"""Implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "a*") ? true
isMatch("aa", ".*") ? true
isMatch("ab", ".*") ? true
isMatch("aab", "c*a*b") ? true"""


class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
#TODO: Still doesnt pass a few tests
        memo = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        memo[0][0] = True
        for i, v in enumerate(p):
            if v == '*' and memo[0][i-1]:
                memo[0][i+1] = True

        for i, v in enumerate(s):
            for j, w in enumerate(p):
                if s[i] == p[j] or p[j] == '.':
                    memo[i+1][j+1] = memo[i][j]
                elif p[j] == '*':
                    if s[i] != p[j-1] and p[j-1] != '.':
                        memo[i+1][j+1] = memo[i][j-1]
                    else:
                        memo[i+1][j+1] = memo[i][j+1] or memo[i+1][j] or memo[i+1][j-1]
                else:
                    memo[i][j] = False

        return memo[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch('aa', 'a'))
    print(solution.isMatch('aa', 'aa'))
    print(solution.isMatch('aaa', 'aa'))
    print(solution.isMatch('aa', 'a*'))
    print(solution.isMatch('aa', '.*'))
    print(solution.isMatch('ab', '.*'))
    print(solution.isMatch('aab', 'c*a*b'))