"""Created by sgoswami on 3/23/17 as part of leetcode"""
"""There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays.
 The overall run time complexity should be O(log (m+n))."""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m1 = self._median_of_a_sorted_list(nums1)
        m2 = self._median_of_a_sorted_list(nums2)
        if m1 < m2 :
            start1 = self._median_index_of_a_sorted_list(nums1)
            start2 = 0
            end1 = len(nums1) -1
            end2 = self._median_index_of_a_sorted_list(nums2)
            return self._find_median_sorted_arrays(nums1, nums2, start1, end1, start2, end2)

        elif m1 > m2:
            start1 = 0
            start2 = self._median_index_of_a_sorted_list(nums2)
            end1 = self._median_index_of_a_sorted_list(nums1)
            end2 = len(nums2) -1
            return self._find_median_sorted_arrays(nums1, nums2, start1, end1, start2, end2)
        else:
            return m1

    def _median_index_of_a_sorted_list(self, nums):
        if len(nums) % 2 == 0:
            return len(nums)/2
        else:
            return len(nums)//2

    def _find_median_sorted_arrays(self, nums1, nums2, start1, end1, start2, end2):
        if start1 - end1 == 1:

            return


