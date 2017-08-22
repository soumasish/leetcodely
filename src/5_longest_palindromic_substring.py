"""Created by sgoswami on 3/23/17 as part of leetcode"""
"""Given a string s, find the longest palindromic substring in s. You may assume that the maximum
length of s is 1000.
Input: 'babad'
Output: 'bab'
Input: 'cbbd'
Output: 'bb'
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        trigger = True
        left, right, len_of_the_curr_palindrome, len_of_the_longest_palindrome = 0, 0, 0, 0
        for i in range(2*len(s)):
            center = i % 2
            if trigger:
                left = center
                right = left + 1
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        len_of_the_curr_palindrome += 2
                        len_of_the_longest_palindrome = max(len_of_the_curr_palindrome, len_of_the_longest_palindrome)
                    else:
                        break
                    left -= 1
                    right +=1
                trigger = not trigger

            else:
                left = center-1
                right = center+1
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        len_of_the_curr_palindrome += 3
                        len_of_the_longest_palindrome = max(len_of_the_curr_palindrome, len_of_the_longest_palindrome)
                    else:
                        break
                    left -= 1
                    right +=1
                trigger = not trigger
        return len_of_the_longest_palindrome

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome('cbbd'))


