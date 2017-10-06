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
        left_product = [1]
        right_product = [1]
        for i in range(1, len(nums)):
            curr_left = left_product[i-1] * nums[i-1]



solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))

