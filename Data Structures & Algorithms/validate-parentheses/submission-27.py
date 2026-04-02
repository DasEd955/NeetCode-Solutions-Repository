class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        #while "()" in s or "{}" in s or "[]" in s:
            #s = s.replace("()", "")
            #s = s.replace("{}", "")
            #s = s.replace("[]", "")
        #return s == ""    

        for char in s:
            if char in closeToOpen.values():
                stack.append(char)
            elif char in closeToOpen:    
                if stack and stack[-1] in closeToOpen[char]:
                    stack.pop()
                else:
                    return False        
        return not stack  
            


        