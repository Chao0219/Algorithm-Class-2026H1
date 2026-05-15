class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        max_val = -float('inf')
        min_val = float('inf')
        amount = 0
        start = -1
        end = 0
        for i in range(len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
            elif nums[i] < max_val:
                end = i
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < min_val:
                min_val = nums[i]
            elif nums[i] > min_val:
                start = i
        if start == -1:
            return 0
        return end - start + 1 
