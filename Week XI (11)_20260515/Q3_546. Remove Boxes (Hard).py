'''
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        memo = {}
        def dfs(i,j,k):
            # i = left; j = right; k=box_far_away
            if i > j: return 0
            if (i, j, k) in memo: return memo[(i, j, k)]
            # cut continue boxes
            get = (k+1)**2 + dfs(i, j-1, 0)
            # find next continuous boxes
            for m in range(i,j):
                if boxes[m] == boxes[j]:
                    get=max(get, dfs(i, m, k+1)+ dfs(m + 1, j - 1, 0))
            memo[(i, j, k)] = get
            return get
        return dfs(0, n-1, 0)
'''
class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        # [1, 1, 2, 2, 2] changed into colors=[1, 2], counts=[2, 3]
        colors = []
        counts = []
        for box in boxes:
            if colors and colors[-1] == box:
                counts[-1] += 1
            else:
                colors.append(box)
                counts.append(1)
                
        n = len(colors)
        
        # record position map of different boxes
        pos_map = {}
        for idx, c in enumerate(colors):
            if c not in pos_map:
                pos_map[c] = []
            pos_map[c].append(idx)
            
        memo = {}
        
        def dfs(i, j, k):
            if i > j: return 0
            if (i, j, k) in memo: return memo[(i, j, k)]
            # cut continue boxes
            res = (counts[j] + k) ** 2 + dfs(i, j - 1, 0)
            
            # find next potential continuous boxes
            current_color = colors[j]
            # finout all color
            all_positions = pos_map[current_color]
            
            # find not contiune boxes
            for m in all_positions:
                if m < i: continue
                if m >= j: break 
                
                # merge non-contiunous boxes
                res = max(res, dfs(m + 1, j - 1, 0) + dfs(i, m, k + counts[j]))
                
            memo[(i, j, k)] = res
            return res
            
        return dfs(0, n - 1, 0)
