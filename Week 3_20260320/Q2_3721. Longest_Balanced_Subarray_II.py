class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        class Node:
            __slots__ = ("l", "r", "mn", "mx", "lazy")
            def __init__(self):
                self.l = self.r = 0
                self.mn = self.mx = 0
                self.lazy = 0
        # tree node 定義
        tree = [Node() for _ in range((n + 1) * 4)]

        # tree node的變數和連結
        def build(u: int, l: int, r: int):
            tree[u].l, tree[u].r = l, r
            tree[u].mn = tree[u].mx = tree[u].lazy = 0
            if l == r:
                return
            ## >>是往小一位 代表/2 這段用來定義父子關係
            mid = (l + r) >> 1
            build(u << 1, l, mid)
            build(u << 1 | 1, mid + 1, r)

        def apply(u: int, v: int):
            tree[u].mn += v
            tree[u].mx += v
            tree[u].lazy += v

        
        
        def pushdown(u: int):
            if tree[u].lazy != 0:
                apply(u << 1, tree[u].lazy)
                apply(u << 1 | 1, tree[u].lazy)
                tree[u].lazy = 0

        def pushup(u: int):
            tree[u].mn = min(tree[u << 1].mn, tree[u << 1 | 1].mn)
            tree[u].mx = max(tree[u << 1].mx, tree[u << 1 | 1].mx)

        # 各個區域進行值的更新
        def modify(u: int, l: int, r: int, v: int):
            if tree[u].l >= l and tree[u].r <= r:
                apply(u, v)
                return
            pushdown(u)
            mid = (tree[u].l + tree[u].r) >> 1
            if l <= mid:
                modify(u << 1, l, r, v)
            if r > mid:
                modify(u << 1 | 1, l, r, v)
            pushup(u)

        # 把左邊跟右邊的平衡值進行調整
        def query(u: int, target: int) -> int:
            if tree[u].l == tree[u].r:
                return tree[u].l
            pushdown(u)
            if tree[u << 1].mn <= target <= tree[u << 1].mx:
                return query(u << 1, target)
            return query(u << 1 | 1, target)

        build(1, 0, n)

        last = {}
        now = ans = 0

        for i, x in enumerate(nums, start=1):
            det = 1 if (x & 1) else -1
            # 定義偶數加1 奇數-1
            if x in last:
                modify(1, last[x], n, -det)
                now -= det
            last[x] = i
            modify(1, i, n, det)
            now += det
            pos = query(1, now)
            ans = max(ans, i - pos)

        return ans
