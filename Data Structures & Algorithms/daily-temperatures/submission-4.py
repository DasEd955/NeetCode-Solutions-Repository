class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = list()
        result = [0] * len(temperatures)

        for i in range(len(result)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                dayCount = i - stack[-1]
                result[stack[-1]] = dayCount
                stack.pop()
            stack.append(i)

        return result    