class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = list()
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token == operators[0]:
                stack.append(stack.pop() + stack.pop())
            elif token == operators[1]:
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == operators[2]:
                stack.append(stack.pop() * stack.pop())
            elif token == operators[3]:            
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(token)) 

        return stack[-1]           