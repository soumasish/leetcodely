"""Created by sgoswami on 6/16/17."""
"""Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product 
of all the elements of nums except nums[i]
Solve it without division and in O(n).
For example, given [1,2,3,4], return [24,12,8,6]."""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a, b, left, right, result = 1, 1, [], [], []

        for i, v in enumerate(nums):
            left.append(a)
            a *= nums[i]

        for i, v in reversed(list(enumerate(nums))):
            right.append(b)
            b *= nums[i]
        right = list(reversed(right))

        for i in range(len(left)):
            result.append(left[i] * right[i])
        return result

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))

