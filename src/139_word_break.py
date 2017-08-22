"""Created by sgoswami on 7/18/17."""

"""Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be 
segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not 
contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code"."""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = [False for _ in range(len(s) + 1)]
        memo[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                print(memo[i])
                print(s[i:j+1])
                if memo[i] and s[i:j+1] in wordDict:
                    memo[j+1] = True
        return memo[-1]

if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak('leetcode', ['leet', 'code']))