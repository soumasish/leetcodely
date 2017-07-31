"""Created by sgoswami on 3/23/17 as part of leetcode"""
"""There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays.
 The overall run time complexity should be O(log (m+n))."""

#TODO: First iteration recursion goes into infinite loop


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return self.findMediaHelper(nums1, nums2, 0, len(nums1)-1, 0, len(nums2) -1)

    def findMediaHelper(self, nums1, nums2, start1, end1, start2, end2):
        if end1 - start1 == 1 and end2 - start2 == 1:
            return (max(nums1[start1], nums2[start2]) + min(nums1[end1], nums2[end2]))//2

        m1_index = (start1 + end1)//2
        m2_index = (start2 + end2)//2

        m1 = nums1[m1_index]
        m2 = nums2[m2_index]

        if m1 == m2:
            return m1

        if m1 < m2:
            start1 = m1_index
            end2 = m2_index
        else:
            start2 = m2_index
            end1 = m1_index
        return self.findMediaHelper(nums1, nums2, start1, end1, start2, end2)

if __name__ == '__main__':
 solution = Solution()