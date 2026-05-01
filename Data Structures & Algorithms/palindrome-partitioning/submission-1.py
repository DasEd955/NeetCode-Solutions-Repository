class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result, palindrome = list(), list()

        def dfs(index: int, s: str) -> None:
            if index == len(s):
                result.append(palindrome.copy())
                return
            
            for j in range(index, len(s)):
                if self.isPalindrome(s[index:j+1]):
                    palindrome.append(s[index:j+1])
                    dfs(j + 1, s)
                    palindrome.pop()
        
        dfs(0, s)
        return result

    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True