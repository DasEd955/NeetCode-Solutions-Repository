class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack, score = list(), 0

        for operation in operations:
            if operation == '+':
                a, b = stack.pop(), stack.pop()
                score = a + b
                stack.append(b)
                stack.append(a)
                stack.append(score)
                print(stack)
                print(score)
            elif operation == 'D':
                a = stack.pop()
                stack.append(a)
                stack.append(a * 2)
                print(stack)
                print(score)
            elif operation == 'C':
                a = stack.pop()
                score -= a
                print(stack)
                print(score)
            else:
                score = int(operation)
                stack.append(score)
                print(stack)
                print(score)
        
        return sum(stack)