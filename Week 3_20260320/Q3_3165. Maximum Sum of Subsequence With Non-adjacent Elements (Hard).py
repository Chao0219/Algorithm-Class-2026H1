class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        # 1. 空間預留與初始化
        tree = [[0] * 4 for _ in range(4 * n)]
        # tree[1]：代表整個陣列 $[0, n-1]$ 的 4 種最大和(merge那裏)狀態。tree[2]：代表左半邊的 4 種狀態。
        # tree[3]：代表右半邊的 4 種狀態。依此類推，tree[node] 的左小孩在 node*2，右小孩在 node*2+1。
        MOD = 10**9 + 7
        INF = float('inf')

        # Divide: 建樹
        def build(node, start, end):
            if start == end:
                # 只剩下一個element 就沒有選誰不選誰的問題了
                val = max(0, nums[start])
                tree[node] = [0, -INF, -INF, val]
                return
            # 對半切
            mid = (start + end) // 2  
            build(node * 2, start, mid) # 父節點*2 是左子
            build(node * 2 + 1, mid + 1, end) #父節點*2+1 是右子
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1]) # 組成樹
        
        
        #  Conquer: 定義如何合併兩個區間的狀態
        def merge(L, R):
            # 對於每一側的子節點 都有頭選尾不選的2 * 2差異
            # 只要注意選左邊尾 不能選右邊頭
            v00 = max(L[0] + R[2], L[1] + R[0], L[0] + R[0])
            v01 = max(L[0] + R[3], L[1] + R[1], L[0] + R[1])
            v10 = max(L[2] + R[2], L[3] + R[0], L[2] + R[0])
            v11 = max(L[2] + R[3], L[3] + R[1], L[2] + R[1])
            return [v00, v01, v10, v11]
        

        # 4. Update: 修改數值
        def update(node, start, end, pos, x):
            if start == end:
                # 只有一個元素就沒有選頭尾不選頭尾的問題
                val = max(0, x)
                tree[node] = [0, -INF, -INF, val]
                return
            mid = (start + end) // 2
            if pos <= mid:
                update(node * 2, start, mid, pos, x)
            else:
                update(node * 2 + 1, mid + 1, end, pos, x)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
            # 子節點變了 所以父節點要重新執行

        # --- 開始執行 ---
        build(1, 0, n - 1)
        total_sum = 0
        
        for pos, xi in queries:
            update(1, 0, n - 1, pos, xi)
            # 整個陣列的最大不相鄰和，必然在根節點的四種選法之一
            total_sum = (total_sum + max(tree[1])) % MOD
            
        return total_sum
