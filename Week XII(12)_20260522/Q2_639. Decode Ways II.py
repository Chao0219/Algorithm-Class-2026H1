class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = [0]*(len(s) + 1) # decode types for fromer i char
        dp[0] += 1 # 假設最前兩個數字可以組成2個一組，就要看前0個字元
        
        for i in range(1, len(s) + 1):
            curr = s[i-1]
        
            # single char
            if curr == '*':
                dp[i] = (dp[i] + dp[i-1] * 9) % MOD
            elif curr != '0': # 1-9
                dp[i] = (dp[i] + dp[i-1] * 1) % MOD
            
            # 2. conbined char
            if i >= 2:
                prev = s[i-2]
            
                if prev == '1':
                    count = 9 if curr == '*' else 1
                    dp[i] = (dp[i] + dp[i-2] * count) % MOD
            
                elif prev == '2':
                    if curr == '*':
                        dp[i] = (dp[i] + dp[i-2] * 6) % MOD
                    elif '0' <= curr <= '6':
                        dp[i] = (dp[i] + dp[i-2] * 1) % MOD
            
                elif prev == '*':
                    if curr == '*':
                        dp[i] = (dp[i] + dp[i-2] * 15) % MOD
                    elif '0' <= curr <= '6':
                        dp[i] = (dp[i] + dp[i-2] * 2) % MOD
                    else:
                        dp[i] = (dp[i] + dp[i-2] * 1) % MOD
                    
        return dp[len(s)]
