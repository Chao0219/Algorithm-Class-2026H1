class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums_ex = [1] + nums + [1]
        n_ex = len(nums_ex)
        dp = [[0] * n_ex for _ in range(n_ex)]
        for length in range(2, n + 2):
            for i in range(n + 2 - length):
                j = i + length
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + (nums_ex[i] * nums_ex[k] * nums_ex[j]))


        return dp[0][n+1]
