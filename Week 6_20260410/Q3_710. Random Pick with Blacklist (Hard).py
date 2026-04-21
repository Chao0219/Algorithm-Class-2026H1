class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        # sorting for searching
        self.black = sorted(blacklist)
        
        self.n_pick = n - len(self.black)

    def pick(self) -> int:
        # pick number randomly
        x = random.randint(0, self.n_pick - 1)

        left, right = 0, len(self.black) - 1
        # finding first black, making black[i] - i > x
        # The number of blacklisted integers we need to skip is exactly 'left'. so we shift i forward
        while left <= right:
            mid = (left + right) // 2
            if self.black[mid] - mid <= x:
                left = mid + 1
            else:
                right = mid - 1
       

        return x + left
