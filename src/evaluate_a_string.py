"""Created by sgoswami on 10/5/17."""
import re
import collections



class Solution:
    def evaluate(self, s: str) -> int:
        expr = [i for i in re.split(r'(\d+|\W+)', s) if i]
        rpn = self.convertToPostfix(expr)
        return self.evalPostfix(rpn)

    def convertToPostfix(self, infix: list) -> list:
        pass


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
                    total = prev // curr
                stack.append(total)
        return stack.pop()
