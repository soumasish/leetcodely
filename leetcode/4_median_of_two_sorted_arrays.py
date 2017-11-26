"""Created by sgoswami on 3/23/17 as part of leetcode"""
"""There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays.
 The overall run time complexity should be O(log (m+n))."""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 or not nums2:
            return -1
        if len(nums1) and len(nums2) == 1:
            return (nums1[0] + nums2[0])/2
        if len(nums1) == 1:
            if len(nums2)% 2 == 0:
                (nums2(len(nums2)//2) + nums2(len(nums2)//2 + 1))/2
            else:
                nums2[len(nums2)//2]
        if len(nums2) == 1:
            if len(nums1) % 2 == 0:
                (nums1(len(nums1) // 2) + nums1(len(nums1) // 2 + 1)) / 2
            else:
                nums1[len(nums1) // 2]

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        return self.findMediaHelper(nums1, nums2, 0, len(nums1)-1, 0, len(nums2) -1)

    def findMediaHelper(self, nums1, nums2, start1, end1, start2, end2):
        if end1 - start1 == 1 and end2 - start2 == 1 or len(nums1) == 1 or len(nums2) == 1:
            return (max(nums1[start1], nums2[start2]) + min(nums1[end1], nums2[end2]))/2
        mid1 = start1 + (end1 - start1)//2
        mid2 = start2 + (end2 - start2)//2

        if nums1[mid1] < nums2[mid2]:
            start1 = mid1
            end2 = mid2
        elif nums1[mid1] > nums2[mid2]:
            start2 = mid2
            end1 = mid1
        else:
            return nums1[mid1] or nums2[mid2]
        return self.findMediaHelper(nums1, nums2, start1, end1, start2, end2)


if __name__ == '__main__':
 solution = Solution()
 print(solution.findMedianSortedArrays([1, 2], [3, 4]))
 print(solution.findMedianSortedArrays([1, 3], [2]))