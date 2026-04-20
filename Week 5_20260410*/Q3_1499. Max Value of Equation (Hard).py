class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # $y_i + y_j + |x_i - x_j|$ & $x_j > x_i$ $
        # Finding maximum $(y_i - x_i) + (y_j + x_j)$
        # Prune and Search, Prune dx > k
        max_val = -float('inf')
        ''' TLE while k goes big
        for i in range(len(points)):
            for j in range((i + 1), len(points)):
                dx = points[j][0] - points[i][0]

                if dx < k: break
                value = (points[i][1] - points[i][0]) + (points[j][1] + points[j][0])
                max_val = max(max_val, current_value)'''
        dq = deque()
        for x_i, y_i in points:
            while dq and x_i - dq[0][1] > k: dq.popleft()
            if dq:
                max_val = max(max_val, dq[0][0] + y_i + x_i)
            current_y_minus_x = y_i - x_i
            while dq and dq[-1][0] <= current_y_minus_x:
                dq.pop()
            dq.append((current_y_minus_x, x_i))
        return max_val
