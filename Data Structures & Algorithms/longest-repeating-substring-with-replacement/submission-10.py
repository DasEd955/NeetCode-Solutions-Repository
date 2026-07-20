class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, longest = 0, 0
        window = dict()

        for right in range(len(s)):
            window[s[right]] = 1 + window.get(s[right], 0)
            while (right - left + 1) - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        
        return longest