class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = list()
        svArray = list()
        
        for i in range(len(position)):
            svTuple = (position[i], speed[i])
            svArray.append(svTuple)

        svArray.sort(reverse=True)

        for car in svArray:
            time = (target - car[0]) / car[1]
            if stack and time <= stack[-1]:
                continue    
            stack.append(time)
        
        return len(stack)
            

        