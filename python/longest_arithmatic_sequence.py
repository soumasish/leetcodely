class Solution:
    def longestArithSeqLength(self, A:[int]) -> int:
        dp = [{0: 1} for _ in range(len(A))]
        res = 1
        for i in range(0, len(A)):
            for j in range(i):
                diff = A[j] - A[i]
                if diff in dp[j]:
                    if diff in dp[i]:
                        dp[i][diff] = max(dp[j][diff] +1, dp[i][diff])
                    else:
                        dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                res = max(res, max(dp[i].values()))
        return res
