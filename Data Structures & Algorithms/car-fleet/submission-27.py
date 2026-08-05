class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack, svArray = list(), list()

        for i in range(len(position)):
            svArray.append([position[i], speed[i]])
        svArray.sort(reverse=True)

        for car in svArray:
            time = (target - car[0]) / car[1]
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        
        return len(stack)

