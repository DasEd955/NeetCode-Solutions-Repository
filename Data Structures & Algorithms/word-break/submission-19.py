class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [None] * (n + 1)
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    if dp[i + len(word)]:
                        dp[i] = True
                        break
            else:
                dp[i] = False
        
        return dp[0]