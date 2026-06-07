class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # Sort arr2 into strickly increase, without repeated array
        arr2 = sorted(list(set(arr2)))
        # Initialize a dict to storage minimum tail number
        dp = {0:-1}
        for x in arr1:
            new_dp = {}
            
            for ops, prev in dp.items():
                # try to save potential change in new_dp, no matter x satisfying strictly increasing locally or not
                if x > prev:
                    new_dp[ops] = min(new_dp.get(ops, float('inf')), x)
                # find number just bigger than prev in arr2
                idx = bisect.bisect_right(arr2, prev)
                if idx < len(arr2):
                    val = arr2[idx]
                    new_dp[ops + 1] = min(new_dp.get(ops + 1, float('inf')), val)
            
            
            if not new_dp:
                return -1
            dp = new_dp
            
        return min(dp.keys())
