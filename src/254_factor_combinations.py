"""Created by sgoswami on 8/9/17."""
"""Numbers can be regarded as product of its factors. For example,
8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors."""
import sys


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # return self.factors(n)
        results = []
        for i in range(2, n):
            if n % i == 0:
                curr_list = [i]


    def get_factors_helper(self, start, finish, array):
        for i in range(start, finish):
            if finish % i == 0:
                array.append(i)
                self.get_factors_helper()


    # def factors(number, max_factor=sys.maxint):
    #     result = []
    #
    #     factor = min(number / 2, max_factor)
    #     while factor >= 2:
    #         if number % factor == 0:
    #             divisor = number / factor
    #
    #             if divisor <= factor and divisor <= max_factor:
    #                 result.append([factor, divisor])
    #
    #             result.extend([factor] + item for item in self.factors(divisor, factor))
    #
    #         factor -= 1
    #
    #     return result



if __name__ == '__main__':
    solution = Solution()
    print(solution.getFactors(32))


