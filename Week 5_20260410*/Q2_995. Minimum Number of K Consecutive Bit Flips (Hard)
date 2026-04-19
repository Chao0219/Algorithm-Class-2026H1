class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flip = 0
        cur_flip = 0
        flip_record = [0] * len(nums)
        for i in range(len(nums)):
            if i >= k :
                cur_flip -= flip_record[i - k]
            if nums[i] % 2 == cur_flip % 2: # 翻轉兩次等於沒翻 不要浪費次數
                if i + k > len(nums) : return -1 # invalid condition
                nums[i] = 1
                flip += 1
                cur_flip +=1
                flip_record[i] = 1
            
        return flip
