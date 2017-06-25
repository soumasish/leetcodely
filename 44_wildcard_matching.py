"""Created by sgoswami on 4/17/17 as part of leetcode"""
"""Implement wildcard pattern matching with support for \'?\' and \'*\'"""
"""'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(s) == 0:
            if len(p) == 0:
                return True
            elif p == '*':
                return True
            else:
                return False
        grid = [[False for _ in range(len(p))] for _ in range(len(s))]
        for i, v in enumerate(grid):
            for j, w in enumerate(grid[i]):
                if s[i] == p[j] or p[j] == '?':
                    if i == 0 and j == 0:
                        grid[i][j] = True
                    if i == 0 or j == 0:
                        grid[i][j] = False
                    else:
                        grid[i][j] = grid[i-1][j-1]
                elif p[i] == '*':
                    if i == 0 and j == 0:
                        grid[i][j] = True
                    if i == 0 or j == 0:
                        if i == 0:
                            grid[i][j] = grid[i][j-1]
                        else:
                            grid[i][j] = grid[i-1][j]

                    else:
                        if grid[i-1][j] is True or grid[i][j-1] is True:
                            grid[i][j] = True

        return grid[-1][-1]
