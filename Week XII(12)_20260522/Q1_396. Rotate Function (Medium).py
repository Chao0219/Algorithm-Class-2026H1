class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ini_sum = sum(nums)
        #F = [0]*len(nums)
        F = 0
        for i in range(len(nums)):
            #F[0] += i*nums[i]
            F += i*nums[i]
        max_f = F

        for i in range(1,len(nums)):
            #F[i]=F[i-1]+ini_sum-len(nums)*nums[-i]
            F = F + ini_sum - len(nums) * nums[-i]
            max_f = max(max_f, F)
        # return max(F)
        return max_f
