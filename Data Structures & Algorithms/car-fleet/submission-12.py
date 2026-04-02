class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        if not position and not speed:
            return 0    

        stack = list()
        svArray = list()
        
        for i in range(len(position)):
            svTuple = (position[i], speed[i])
            svArray.append(svTuple)

        svArray.sort(reverse=True)

        if len(svArray) == 1:
            return 1

        #print(svArray)
        for car in svArray:
            time = (target - car[0]) / car[1]
            if stack and time <= stack[-1]:
                continue
            if time not in stack:    
                stack.append(time)
        
        print(stack)
        return len(stack)
            

        