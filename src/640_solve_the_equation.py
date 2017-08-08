"""Created by sgoswami on 8/6/17."""
"""Solve a given equation and return the value of x in the form of string "x=#value". 
The equation contains only '+', '-' operation, the variable x and its coefficient.
If there is no solution for the equation, return "No solution".
If there are infinite solutions for the equation, return "Infinite solutions".
If there is exactly one solution for the equation, we ensure that the value of x is an integer."""
import re


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        lhs = equation.split('=')[0]
        rhs = equation.split('=')[1]

        p_coeff = re.compile('-?\d*x')
        p_num = re.compile('-\d*')

        lhs_coeff = p_coeff.findall(lhs)
        lhs_num = p_num.findall(lhs)

        rhs_coeff = p_coeff.findall(rhs)
        rhs_num = p_num.findall(rhs)

