"""Created by sgoswami on 3/23/17 as part of leetcode"""
"""Given a string, find the length of the longest substring without repeating characters.
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
subsequence and not a substring."""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        items = []
        char_map = {}
        index = 0
        for c in s:
            if c in char_map:
                if c in items:
                    deduction = char_map[c] + 1
                    items = items[char_map[c]+1:]
                    char_map[c] = index
                    index -= deduction
                    self._update_keys(char_map, deduction)
            items.append(c)
            max_length = max(len(items), max_length)
            char_map[c] = index
            index += 1
        return max_length

    def _update_keys(self, map, num):
        for k, v in map.items():
            v -= num


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("bpfbhmipx"))

