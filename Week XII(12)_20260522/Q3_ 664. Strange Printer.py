class Solution:
    def strangePrinter(self, s: str) -> int:
        if len(s) == 0: return 0
        dp = [[0] * len(s) for _ in range(len(s))]
        # from i to j, switch needed
        for i in range(len(s)):
            dp[i][i] = 1
        for length in range(2, len(s)+1):
            for i in range(len(s)- length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j]=float('inf')
                    for k in range(i,j):
                        dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j])
        return dp[0][len(s)-1]
