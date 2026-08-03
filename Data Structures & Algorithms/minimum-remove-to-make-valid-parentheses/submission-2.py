class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result, stack = list(s), list()

        for i, char in enumerate(result):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    result[i] = ''
        
        while stack:
            result[stack.pop()] = ''
        
        return ''.join(result)