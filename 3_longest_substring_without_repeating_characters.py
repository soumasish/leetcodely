"""Created by sgoswami on 3/23/17 as part of leetcode"""
"""Given a string, find the length of the longest substring without repeating characters.
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a
subsequence and not a substring.
Given bpfbhmipx the answer is 7."""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        checklist = {}
        starting_index_of_current_substring = 0
        length_of_longest_substring = 0
        for i, v in enumerate(s):
            if v in checklist:
                if checklist[v] >= starting_index_of_current_substring:
                    starting_index_of_current_substring = checklist[v] + 1

            length_of_current_substring = i - starting_index_of_current_substring + 1
            length_of_longest_substring = max(length_of_current_substring, length_of_longest_substring)
            checklist[v] = i
        return length_of_longest_substring


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
