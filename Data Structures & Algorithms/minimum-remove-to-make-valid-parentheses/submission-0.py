class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        closeToOpen = {')' : '('}
        stack, remove = list(), set()

        for i in range(len(s)):
            if s[i] in closeToOpen:
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
            elif s[i] in closeToOpen.values():
                stack.append(i)
        
        while stack:
            remove.add(stack.pop())

        result = list()
        for i, char in enumerate(s):
            if i not in remove:
                result.append(char)
        
        return "".join(result)