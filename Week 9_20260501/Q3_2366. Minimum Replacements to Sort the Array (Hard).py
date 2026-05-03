class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # Aim : Non decreasing
        # Important :　Check　Decreasing
        convert = 0
        new_array = []
        biggest = nums[len(nums)-1]
        # 不要強求去更新陣列,因為陣列immutable,會花太多空間和時間
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > biggest:
                # 在設有biggest為值得上界進行平均分配
                share = (nums[i] + biggest - 1 )// biggest
                # 直接推算分配次數，而不是做一個算一個
                convert += (share - 1)
                biggest = nums[i] // share
            else:
                biggest= nums[i]

        return convert
