from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        dp = [0 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1], dp[-2])
