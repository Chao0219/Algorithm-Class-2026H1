class Solution:
    def partitionString(self, s: str) -> int:
        unique = 1 # a least 1 unique substring
        seg = set()
        for i in range(len(s)):
            if s[i] in seg:
                unique += 1
                seg = set()
            seg.add(s[i])
        return unique
