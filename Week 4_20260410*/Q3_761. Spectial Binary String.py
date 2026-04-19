class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s : return ''
        balance = 0
        star = 0
        end = 0
        array=[]
        for i, char in enumerate(s):
            # Balancing
            if char == '1':
                balance += 1
            else:
                balance -= 1
            
            if balance == 0:
                inner_max = self.makeLargestSpecial(s[star + 1 : i])
                array.append('1' + inner_max + "0")
                star = i + 1
            else: continue
        return "".join(sorted(array, reverse=True))
