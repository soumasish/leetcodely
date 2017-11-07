"""Created by sgoswami on 8/8/17."""
"""Given a collection of distinct numbers, return all possible permutations."""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    #     result = []
    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if i != j:
    #                 temp = self.swap(i, j, nums)
    #                 # print(temp)
    #                 result.append(temp)
    #     return result
    #
    # def swap(self, i, j, arr):
    #     arr[i], arr[j] = arr[j], arr[i]
    #     res = arr[:]
    #     arr[i], arr[j] = arr[j], arr[i]
    #     return res



        # perms = [[]]
        # for num in nums:
        #     curr = []
        #     for perm in perms: #to every list
        #         for i in range(len(perm) + 1): #in all positions
        #             curr.append(perm[:i] + [num] + perm[i:])
        #     perms = curr
        # return perms

        # perms = [[]]
        # for n in nums:
        #     new_perms = []ans = set()
        #
        #     for perm in perms:
        #         for i in range(len(perm) + 1):
        #             new_perms.append(perm[:i] + [n] + perm[i:])  ###insert n
        #     perms = new_perms
        # return perms

if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3, 4]))
