'''$O(n^2 \cdot k)$
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums)+1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        dp = [[float('inf')] * (k + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = 0
        for i in range(1, len(nums)+1):
            dp[i][1] = prefix_sum[i]

        for i in range(1,len(nums)+1):
            for j in range(2, k+1):
                if j > i:
                    break
                for p in range(j-1, i):
                    left_sum = dp[p][j-1]
                    right_sum = prefix_sum[i]-prefix_sum[p]
                    dp[i][j] = min(dp[i][j], max(left_sum, right_sum))
        return dp[len(nums)][k]
'''
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low < high:
            mid = (low + high) // 2
            split = 1
            curr_split = 0
            for num in nums:
                if curr_split + num > mid:
                    split += 1
                    curr_split = num
                else:
                    curr_split += num
            if split > k:
                low = mid + 1
            else:
                high = mid
        return high
