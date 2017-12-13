"""Created by sgoswami on 8/9/17."""
"""Find the contiguous subarray within an array (containing at least one number) which has the largest product.
For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6."""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_product, max_product, min_product = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            curr_product *= nums[i]
            max_product = max(max_product, curr_product)
            if curr_product < 0:
                curr_product = 1
        return max_product
    

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct([-2]))

