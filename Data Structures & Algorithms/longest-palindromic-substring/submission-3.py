class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s: str) -> list[int]:
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0] * n
            left, right = 0, 0
            for i in range(n):
                p[i] = min(right - i, p[left + (right - i)]) if i < right else 0
                while(i + p[i] + 1 < n and i - p[i] - 1 >= 0
                      and t[i + p[i] + 1] == t[i - p[i] - 1]):
                    p[i] += 1
                if i + p[i] > right:
                    left, right = i - p[i], i + p[i]
            return p
        
        p = manacher(s)
        resLen, centerIdx = max((v, i) for i, v in enumerate(p))
        resIdx = (centerIdx - resLen) // 2
        return s[resIdx : resIdx + resLen] 