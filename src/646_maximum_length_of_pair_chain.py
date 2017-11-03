"""Created by sgoswami on 10/8/17."""
"""You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.
Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed 
in this fashion.
Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. 
You can select pairs in any order."""


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        curr_length = 0
        for i in range(len(pairs)):
            res = [pairs[i]]
            curr = pairs[i]
            for j in range(len(pairs)):
                if j != i:
                    if pairs[j][0] > curr[1]:
                        res.append(pairs[j])
                        curr = pairs[j]
            curr_length = max(curr_length, len(res))
        return curr_length


if __name__ == '__main__':
    solution = Solution()
    print(solution.findLongestChain([[-10, -8],[8, 9],[-5, 0],[6, 10],[-6, -4],[1, 7],[9, 10],[-4, 7]]))


