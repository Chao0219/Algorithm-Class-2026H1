class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        # 不可以出現等差數列 所以可能要用擴張的
        # from discussion : 奇數+奇數=2*奇數or2*偶數,所以先排除掉偶數穿插奇數之中
        # 先從最小的開始
        res = [1]
        while len(res) < n:
            # 每一個array生出2x-1, 2x數字 (奇數,偶數) 構成的新list 再把他接起來
            res = [2 * x - 1 for x in res] + [2 * x for x in res]
    
        # 把<=n的抓出來
        return [x for x in res if x <= n]
