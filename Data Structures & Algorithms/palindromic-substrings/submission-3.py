class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        palindromes = 0

        def tryCenterPalindrome(left: int, right: int) -> int:
            total = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                total += 1
            return total
        
        for i in range(len(s)):
            palindromes += tryCenterPalindrome(i, i)
            palindromes += tryCenterPalindrome(i, i+ 1)
            
        return palindromes