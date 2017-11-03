"""Created by sgoswami on 10/5/17."""
import re
import collections


class Solution:
    def evaluate(self, s: str) -> int:
        expr = [i for i in re.split(r'(\d+|\W+)', s) if i]
        rpn = self.convertToPostfix(expr)
        return self.evalPostfix(rpn)

    def convertToPostfix(self, infix: list) -> list:
        stack = collections.deque()
        result = []
        for item in infix:
            if item.isdigit():
                result.append(item)
            else:
                while len(stack) > 0 and self.has_higher_precedence(stack[-1], item):
                    result.append(stack[-1])
                    stack.pop()
                stack.append(item)
        while len(stack) > 0:
            result.append(stack.pop())
        return result

    def has_higher_precedence(self, a: str, b: str) -> bool:
        if a == '/' and b == '*' or b == '+' or b == '-':
            return True
        if a == '*' and b == '+' or '-':
            return True
        if a == '+' and b == '-':
            return True
        return False

    def evalPostfix(self, p: list) -> int:
        stack = collections.deque()
        for item in p:
            if item.isdigit():
                stack.append(int(item))
            elif item[1:].isdigit():
                stack.append(int(item))
            else:
                curr = stack.pop()
                prev = stack.pop()
                if item == '+':
                    total = prev + curr
                elif item == '-':
                    total = prev - curr
                elif item == '*':
                    total = prev * curr
                else:
                    total = prev / curr
                stack.append(total)
        return stack.pop()

if __name__ == '__main__':
    solution = Solution()
    print(solution.evaluate('3+12-7/4*3'))
