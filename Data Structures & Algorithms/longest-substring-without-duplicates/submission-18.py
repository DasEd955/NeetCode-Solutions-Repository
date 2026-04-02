class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        window, longest = set(), 0
        left = 0

        for right in range(left, len(s)):
                while s[right] in window:
                        window.remove(s[left])
                        left += 1
                window.add(s[right])        
                longest = max(longest, len(window))

        return longest                                        
        
        