class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        sl = SortedList()
        # SortedList是外面引進來的函數 會自動排序
        idx = SortedList(range(n)) # List長度
        inv = 0
        for i in range(n - 1):
            sl.add((nums[i] + nums[i + 1], i)) # 和鄰居加好以後存下值與位置
            if nums[i] > nums[i + 1]:
                inv += 1 # 偵測數列是否具有decreasing；有幾個
        # 最小的一定會被加掉
        ans = 0
        while inv: #若數列還有decreasing對
            ans += 1
            s, i = sl.pop(0) # 丟進Sortlist排序好就可以知道誰最小了 s是值 i 是位置
            pos = idx.index(i) # 知道位置哪裡要被動
            j = idx[pos + 1]
            if nums[i] > nums[j]:
                inv -= 1
            if pos > 0: #要來交換element了
                h = idx[pos - 1] #左邊
                if nums[h] > nums[i]:
                    inv -= 1 #再檢查
                sl.remove((nums[h] + nums[i], h)) #交換完了要拿掉數字
                if nums[h] > s:
                    inv += 1 #再檢查
                sl.add((nums[h] + s, h)) #加完數字拿回去
            if pos + 2 < len(idx): #右邊鄰居
                k = idx[pos + 2]
                if nums[j] > nums[k]:
                    inv -= 1 #再檢查
                sl.remove((nums[j] + nums[k], j))
                if s > nums[k]:
                    inv += 1 #再檢查
                sl.add((s + nums[k], i))

            nums[i] = s
            idx.remove(j)
        return ans


# 本來的n-square寫法
'''class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        nums1=[]
        
        while True :
            sorted = True
            for i in range(len(nums)-1) :
                if nums[i] > nums[i+1]:
                    sorted = False
            if sorted :
                return count
            # 單純比大小並取代
            sum = float('inf')
            tridx = len(nums)
            for j in range(len(nums)-1) : 
                if nums[j] + nums [j+1] < sum:
                    sum = nums[j] + nums[j+1]
                    tridx = j
                
            nums1 = nums[:tridx]
            nums1.append(sum)
            nums1 = nums1 + nums[tridx+2 : ]
            count += 1
            nums = nums1
            
        return count
        '''