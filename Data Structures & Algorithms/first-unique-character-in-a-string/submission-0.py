class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = dict()

        for char in s:
            seen[char] = 1 + seen.get(char, 0)
        
        for i, char in enumerate(s):
            if seen[char] == 1:
                return i
        
        return -1