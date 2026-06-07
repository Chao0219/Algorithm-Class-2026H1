class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # times availble to test for a pig  = minutesToTest/minutesToDie
        T = minutesToTest // minutesToDie
        # (T+1)^(pigs) should >= buckets for all buckets to be tested
        return math.ceil(math.log(buckets) / math.log(T + 1) - 1e-10)
