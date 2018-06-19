"""Created by sgoswami on 3/23/17 as part of leetcode"""
"""There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays.
 The overall run time complexity should be O(log (m+n))."""
from statistics import mean


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        pass




if __name__ == '__main__':
    arr1 = [1, 7, 13, 21, 27, 29, 32]
    arr2 = [2, 3, 4, 9, 12, 14, 23]
    solution = Solution()
    print(solution.findMedianSortedArrays(arr1, arr2))
