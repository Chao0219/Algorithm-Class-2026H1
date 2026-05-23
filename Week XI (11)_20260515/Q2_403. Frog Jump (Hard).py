'''
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        stone_map = {pos: idx for idx, pos in enumerate(stones)}
        dp = [[0 for _ in range(len(stones))] for _ in range(len(stones))]
        
        dp[0][0] = 1
        for i in range(len(stones)):
            for k in range(len(stones)):
                if dp[k][i] == 1:
                    for diff in[-1,0,1]:
                        next_k = k + diff
                        if next_k > 0:
                            target_pos = stones[i] + next_k
                            if target_pos in stone_map:
                                target_idx = stone_map[target_pos]
                                dp[next_k][target_idx] = 1
                                    
        return any(dp[k][len(stones)-1] == 1 for k in range(len(stones)))
'''
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
            
        stone_map = {pos: idx for idx, pos in enumerate(stones)}
        target_idx = len(stones) - 1

        @cache
        def dfs(i: int, k: int) -> bool:
            # 成功抵達最後一顆石頭，立刻通關！
            if i == target_idx:
                return True
                
            # 遍歷下一步的三種步伐
            for diff in [-1, 0, 1]:
                next_k = k + diff
                if next_k > 0:
                    target_pos = stones[i] + next_k
                    if target_pos in stone_map:
                        # 遞迴探索下一顆石頭
                        if dfs(stone_map[target_pos], next_k):
                            return True # 只要有一條路通，就是成功
                            
            return False # 走遍所有分支都通往死胡同

        # 起始點：在 index 1（位置1），上一步步伐是 1
        return dfs(1, 1)
