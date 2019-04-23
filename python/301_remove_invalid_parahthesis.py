"""Created by sgoswami on 7/2/17."""

"""Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
Note: The input string may contain letters other than the parentheses ( and )."""
import collections


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        queue = collections.deque()
        
        # queue = collections.deque()
        # queue.appendleft(s)
        # results = set()
        # while len(queue) > 0:
        #     curr_str = queue.pop()
        #     for i in range(len(curr_str)):
        #         modified_str = curr_str[:i] + curr_str[i+1:]
        #         if self.check_valid(modified_str):
        #             results.add(modified_str)
        #         else:
        #             queue.appendleft(modified_str)
        #     if len(results) > 0:
        #         break
        # return list(results)


    #     result = set([])
    #     queue = collections.deque()
    #     queue.appendleft(s)
    #     while len(queue) > 0:
    #         curr, modified = queue.pop(), ''
    #         for i, v in enumerate(curr):
    #             if v == '(' or v == ')':
    #                 if i < len(curr) - 1:
    #                     modified = curr[:i] + curr[i + 1:]
    #                 else:
    #                     modified = curr[:-1]
    #             if self.check_valid(modified):
    #                 result.add(modified)
    #         if len(result) > 0:
    #             break
    #         else:
    #             stripped = self.strip_first_paranthesis(curr)
    #             queue.appendleft(stripped)
    #     return list(result)
    #
    # #TODO : Fix this one to cater to edge cases
    # def strip_first_paranthesis(self, s):
    #     for i, v in enumerate(s):
    #         if v == '(' or v == ')':
    #             if i < len(s) - 1:
    #                 s = s[:i] + s[i + 1:]
    #             else:
    #                 s = s[:-1]
    #             break
    #     return s
    #
    def check_valid(self, s):
        stack = []
        for i, v in enumerate(s):
            if v == '(':
                stack.append(v)
            elif v == ')':
                if len(stack) == 0:
                    return False
                elif stack[-1] != '(':
                    return False
                else:
                    stack.pop()
        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeInvalidParentheses("()())()"))
