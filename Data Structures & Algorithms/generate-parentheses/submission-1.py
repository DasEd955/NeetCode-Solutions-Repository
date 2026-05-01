class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result, current = list(), list()
        openCount = closeCount = 0

        def dfs(openCount: int, closeCount: int, current: list[str]) -> None:
            if len(current) == n * 2:
                result.append(''.join(current))
                return 
            
            if openCount < n:
                current.append('(')
                dfs(openCount+1, closeCount, current)
                current.pop()

            if closeCount < openCount:
                current.append(')')
                dfs(openCount, closeCount+1, current)
                current.pop()
            
        dfs(0, 0, current)
        return result
        
