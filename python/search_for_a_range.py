"""Created by sgoswami on 8/20/17."""
"""Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4]"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = 0, len(nums) - 1
        while nums[start] < nums[end]:
            mid = start + (end - start)//2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
            else:
                if nums[start] == nums[mid]:
                    end -= 1
                elif nums[end] == nums[mid]:
                    start += 1

        if nums[start] == nums[end] == target:
            return [start, end]
        return [-1, -1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))
