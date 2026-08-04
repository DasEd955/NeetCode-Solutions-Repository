class Solution:
    def decodeString(self, s: str) -> str:
        stringStack, countStack = list(), list()
        curr, k = str(), 0

        for char in s:
            if char.isdigit():
                k = k * 10 + int(char)
            elif char == '[':
                stringStack.append(curr)
                countStack.append(k)
                curr, k = str(), 0
            elif char == ']':
                temp = curr
                curr = stringStack.pop()
                count = countStack.pop()
                curr += temp * count
            else:
                curr += char
        
        return curr