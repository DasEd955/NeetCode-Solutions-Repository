class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        current = 0
        one, two = 1, 0
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                current = 0
            else:
                current = one
            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                current += two
            two = one
            one = current
        
        return current