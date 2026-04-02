class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        closeToOpen = {")" : "(", "]" : "[", "}": "{"}

        for char in s:
            if char in closeToOpen.values():
                stack.append(char)
            elif char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
        return not stack            


        