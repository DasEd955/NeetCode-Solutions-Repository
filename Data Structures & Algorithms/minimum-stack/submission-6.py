class MinStack:

    def __init__(self):
        self.stack = list()
        self.minStack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        #self.minStack.append(val)
        if self.minStack:     
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)    

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        #return min(self.stack)
        return self.minStack[-1]

        
