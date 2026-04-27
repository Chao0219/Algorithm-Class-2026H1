class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_idx = 0
        p_idx = 0

        last_s_idx = 0
        last_p_star_idx = -1
        
        while s_idx < len(s):
            # match and ?
            if p_idx < len(p) and (p[p_idx] == s[s_idx] or p[p_idx] == '?'):
                s_idx += 1
                p_idx += 1
            # *
            elif p_idx < len(p) and p[p_idx] == '*':
                last_p_star_idx = p_idx
                last_s_idx = s_idx
                p_idx += 1
            # former idx
            elif last_p_star_idx != -1:
                last_s_idx += 1
                s_idx = last_s_idx
                p_idx = last_p_star_idx + 1
            # non match at all
            else:
                return False
        while p_idx < len(p) and p[p_idx] == '*':
            p_idx += 1
        return p_idx == len(p)
