class Solution:
    def numDecodings(self, s: str) -> int:

        memo = [-1] * len(s)

        def backtrack(i: int) -> int:
            if i >= len(s):
                return 1
            if s[i] == '0':
                return 0
            if memo[i] != -1:
                return memo[i]
            ways = backtrack(i + 1)
            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                ways += backtrack(i + 2)
            memo[i] = ways
            return ways
        
        return backtrack(0)