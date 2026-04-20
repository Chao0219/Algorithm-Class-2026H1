class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        min_val = 5001
        while low < high: # 停止的邊界條件
            mid = (low + high) // 2
            # Prune
            if nums[mid] > nums[high]:
                low = mid + 1
                # 只比右邊
            elif nums[mid] < nums[high]:
                high = mid
                # 只比左邊
            else:
                 high -= 1 # 相等情況
        return nums[low]
