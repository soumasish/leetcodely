"""Created by sgoswami on 10/2/17."""
"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not."""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def _match(c, t):
            if c == '(' and t == ')':
                return True
            if c == '{' and t == '}':
                return True
            if c == '[' and t == ']':
                return True
            return False

        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')' or c == '}' or c == ']':
                if len(stack) > 0 and _match(stack[-1], c):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0



if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('()[]{}'))
