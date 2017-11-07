"""Created by sgoswami on 9/13/17."""
"""Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5."""
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = []
        for num in nums:
            heapq.heappush(pq, num)

        return heapq.nlargest(k, pq)[-1]
