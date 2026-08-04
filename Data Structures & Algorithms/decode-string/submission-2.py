class Solution:
    def decodeString(self, s: str) -> str:
        stringStack, countStack = list(), list()
        curr, k = list(), 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                stringStack.append(curr)
                countStack.append(k)
                curr, k = list(), 0
            elif char == ']':
                prev = stringStack.pop()
                count = countStack.pop()
                curr = prev + (curr * count)
            else:
                curr.append(char)
        
        return ''.join(curr)