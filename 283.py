"""Created by sgoswami on 3/7/17 as part of leetcode"""

"""Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0]."""


class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        non_zero_index = []

        for i in range(len(nums)):
            if nums[i] != 0:
                non_zero_index.append(i)
        z = 0
        for i in range(len(nums)):
            if z < len(non_zero_index):
                nums[z] = nums[non_zero_index[i]]
                z += 1
            else:
                nums[i] = 0


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    print(solution.moveZeroes(nums))




