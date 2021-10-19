"""Created by sgoswami on 3/23/17 as part of leetcode"""
import statistics

"""There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays.
 The overall run time complexity should be O(log (m+n))."""
import sys
import unittest


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        final = []  # array for storing the other 2 arrays after sorting them
        i = j = 0

        # below code is similar to merge sort
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                final.append(nums1[i])
                i += 1
            else:
                final.append(nums2[j])
                j += 1
        while i < m:
            final.append(nums1[i])
            i += 1
        while j < n:
            final.append(nums2[j])
            j += 1

        # finally, finding the median of the sorted array using median function from statistics
        return statistics.median(final)


class TestSolution(unittest.TestCase):

    def test_one(self):
        self.assertEqual(Solution().findMedianSortedArrays(nums1=[1, 3], nums2=[2]), 2.000)

    def test_two(self):
        self.assertEqual(Solution().findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]), 2.000)

    def test_three(self):
        self.assertEqual(Solution().findMedianSortedArrays(nums1=[0, 0], nums2=[0, 0]), 2.000)

    def test_four(self):
        self.assertEqual(Solution().findMedianSortedArrays(nums1=[], nums2=[1]), 2.000)

    def test_five(self):
        self.assertEqual(Solution().findMedianSortedArrays(nums1=[2], nums2=[]), 2.000)


unittest.main(exit=False)
