class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        sweap = 0
        pos = {val: i for i, val in enumerate(row)}
        # Storage the pos map, by applying enmerate to output(index, value)
        for i in range(0, len(row),2):
            target = row[i] ^ 1
            # 很玄的 XOR：0->1, 1->0, 2->3, 3->2
            if row[i+1] != target :
                # output pos of target
                target_idx = pos[target]
                # exchange
                whom2change = row[i+1]
                pos[whom2change] = target_idx
                row[i+1], row[target_idx] = row[target_idx], row[i+1]
                sweap += 1
                
        return sweap
