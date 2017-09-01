"""Created by sgoswami on 7/18/17."""

"""Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be 
segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not 
contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code"."""
import collections

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # Modeled as a graph problem - every index is a vertex and every edge is a completed word
        # The problem thus boils down to if a path exists.

        queue = collections.deque()
        visited = set()
        queue.appendleft(0)
        visited.add(0)
        while len(queue) > 0:
            curr_index = queue.pop()
            for i in range(curr_index, len(s)+1):
                if i in visited:
                    continue
                if s[curr_index:i] in wordDict:
                    if i == len(s):
                        return True
                    queue.appendleft(i)
                    visited.add(i)
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.wordBreak('leetcode', ['leet', 'code']))