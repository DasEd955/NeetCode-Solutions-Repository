class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        seenChars = set()

        for right in range(len(s)):
            while s[right] in seenChars:
                seenChars.remove(s[left])
                left += 1
            seenChars.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest