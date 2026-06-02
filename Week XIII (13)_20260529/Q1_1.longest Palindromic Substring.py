class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s
        start=0
        max_len = 1
        # 以每一個元素為中心 往左右找
        def expand(left: int, right:int):
            while left >=0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left -1

        for i in range(n):
            len1 = expand(i,i)
            len2 = expand(i, i + 1)

            current_max = max(len1, len2)

            if current_max > max_len:
                max_len = current_max

                start = i - (current_max -1) // 2

        return s[start : start+max_len]
