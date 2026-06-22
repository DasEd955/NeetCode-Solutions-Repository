class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        longest = str()

        def tryCenterPalindrome(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        for i in range(len(s)):
            palindromeOdd = tryCenterPalindrome(i, i)
            if len(palindromeOdd) > len(longest):
                longest = palindromeOdd
            palindromeEven = tryCenterPalindrome(i, i + 1)
            if len(palindromeEven) > len(longest):
                longest = palindromeEven
        
        return longest