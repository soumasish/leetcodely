"""Created by sgoswami on 7/5/17."""
"""Given a digit string, return all possible letter combinations that the number could represent."""

class Solution(object):
    def __init__(self):
        self.digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
