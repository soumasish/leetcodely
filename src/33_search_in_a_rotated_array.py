"""Created by sgoswami on 8/2/17."""

"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array."""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums)-1
        while start < end:
            mid = start + (end - start)//2
            if nums[mid] < nums[end]:
                end = mid - 1
            else:
                start = mid + 1
        pivot = start

        while start <= end:
            mid = start + (end - start)//2
            real_mid = (mid + pivot) % len(nums)
            if target < nums[real_mid]:
                start = mid
            elif target > nums[real_mid]:
                end = mid - 1
            else:
                return real_mid
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.search([17, 19, 20, 2, 3, 4, 9, 11, 13, 14], 9))

