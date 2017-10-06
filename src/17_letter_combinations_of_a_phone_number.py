"""Created by sgoswami on 7/5/17."""
"""Given a digit string, return all possible letter combinations that the number could represent."""
import collections


class Solution(object):
    def __init__(self):
        self.digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        



    #     combinations = set()
    #     return self.helper(digits, '', combinations)
    #
    # def helper(self, rest_of_the_digits, path_so_far, combinations):
    #     # if not rest_of_the_digits:
    #     #     combinations.add(path_so_far)
    #     #     return
    #     # first, rest = rest_of_the_digits[0], rest_of_the_digits[1:]
    #     # letters = self.digit_map[first]
    #     # for letter in letters:
    #     #     self.helper(rest, path_so_far+letter, combinations)
    #     #
    #     # return combinations
    #     if not rest_of_the_digits:
    #         combinations.add(path_so_far)
    #         return
    #     first, rest = rest_of_the_digits[0], rest_of_the_digits[1:]
    #     letters = self.digit_map[first]
    #     for l in letters:
    #         self.helper(rest_of_the_digits, path_so_far + l, combinations)

if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('23'))
