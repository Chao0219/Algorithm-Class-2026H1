class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # next station = gasremain[i] + gas[i] - cos[i]
        gas_now = 0
        gas_add = 0
        start_idx = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            gas_add += diff
            gas_now +=diff

            if gas_now < 0:
                start_idx = i + 1
                gas_now = 0
                gas_add = 0
        return start_idx
