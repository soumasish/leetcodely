"""Created by sgoswami on 7/31/17."""
"""Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true."""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {},{}
        for v, w in zip(s, t):
            if v in d1 and d1[v] != w or w in d2 and d2[w] != v:
                return False
            d1[v] = w
            d2[w] = v
        return True

