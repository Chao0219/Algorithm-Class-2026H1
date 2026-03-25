class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        out = []
        def merge_sort(array):
            if len(array) == 0 :return array
            if len(array) == 1 :return array

            # divide
            mid = len(array) // 2
            left = merge_sort(array[:mid])
            right = merge_sort(array [mid:])
            result =[]

    
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] > right[j] :
                    result.append(right[j])
                    j += 1
                else : 
                    result.append(left[i])
                    i += 1

            result += (left[i:])
            result += (right[j:])

            return result
        
        sorted_nums_copy = merge_sort(nums)

        # 分割與反轉
        n = len(nums)
        mid = (n + 1) // 2
        nums1 = sorted_nums_copy[:mid]
        nums2 = sorted_nums_copy[mid:]
        nums1.reverse()
        nums2.reverse()

        # 3. 建立結果並「原地」更新
        # 為了避免你擔心的指標問題，我們直接建立一個暫存列表
        res = [0] * n
        p1 = 0
        p2 = 0
        for i in range(n):
            if i % 2 == 0:
                res[i] = nums1[p1]
                p1 += 1
            else:
                res[i] = nums2[p2]
                p2 += 1
        
        # 關鍵：這行會把 res 的內容塞回 LeetCode 監控的 nums 記憶體裡
        nums[:] = res

