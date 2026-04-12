class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        if len(buildings) == 1:
            l, r, h = buildings[0]
            return [[l, h], [r, 0]]
        
        # Divide
        mid = len(buildings) // 2
        left_skyline = self.getSkyline(buildings[:mid])
        right_skyline = self.getSkyline(buildings[mid:])
        return self.merge(left_skyline, right_skyline)

    def merge(self, left, right):
        h1, h2 = 0, 0
        i, j = 0, 0
        res = []
        
        while i < len(left) and j < len(right):
            
            if left[i][0] < right[j][0]:
                # 找左邊建築端點
                x, h1 = left[i]
                i += 1
            elif left[i][0] > right[j][0]:
                # 找右邊建築端點
                x, h2 = right[j]
                j += 1
            else:
                # 讀取左右建築相交的點
                x, h1 = left[i]
                _, h2 = right[j] # 取得右邊高度，並移動指標
                i += 1
                j += 1
            
            # 決定當前最高高度
            curr_max = max(h1, h2)
            
            # 不能有連續相同高度的水平線段
            if not res or res[-1][1] != curr_max:
                res.append([x, curr_max])
        
        # 剩下的建築
        res.extend(left[i:])
        res.extend(right[j:])
        return res
