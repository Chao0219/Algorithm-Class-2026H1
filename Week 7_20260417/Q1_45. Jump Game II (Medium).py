class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0
        curr_end = 0
        next_far = 0
        
        if len(nums) <= 1 :return 0
        
        for i in range(len(nums)-1):
            next_far = max(next_far, i + nums[i])
            
            if i == curr_end:
                jump += 1           
                curr_end = next_far  
                if curr_end >= len(nums) - 1:
                    break
        return jump
                
