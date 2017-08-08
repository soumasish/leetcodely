"""Created by sgoswami on 8/7/17."""
"""Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array.
 Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their 
 absolute difference is k."""
import collections


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        value_map = collections.Counter(nums)
        pairs = set()
        for item in nums:
            if k == 0:
                if value_map[item] > 1:
                    pairs.add((item, item))

                elif -item in value_map:
                    pairs.add((item, -item))

            else:
                if item + k in value_map:
                    pairs.add((item, item+k))
        return len(pairs)

if __name__ == '__main__':
    solution = Solution()
    print(solution.findPairs([3,1,4,1,5], 2))
