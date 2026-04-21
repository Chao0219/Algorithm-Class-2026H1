class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        men = sorted(zip(efficiency, speed), reverse = True)

        min_heap = []
        total_speed = 0
        ans = 0

        for e, s in men:
            heapq.heappush(min_heap, s)
            total_speed += s
            if len(min_heap) > k:
                
                slowest_speed = heapq.heappop(min_heap)
                total_speed -= slowest_speed

            
            ans = max(ans, total_speed * e)

        return ans % (10**9 + 7)
