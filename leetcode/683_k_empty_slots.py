class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        status = [0 for _ in range(len(flowers))]
        for i in range(len(flowers)):
            status[flowers[i]] = 1
            l, m, count = flowers[i], flowers[i], 0
            while l >= 0 and m < len(flowers) and count < k + 1:
                if status[l] == 1 or status[m] == 1:
                    break
                if status[l] == 1 or status[m] == 1 and count == k:
                    return i
                l -= 1
                m += 1
                count += 1
        return -1

if __name__ == '__main__':
    solution = Solution()
    print(solution.kEmptySlots([1, 3, 2], 1))
