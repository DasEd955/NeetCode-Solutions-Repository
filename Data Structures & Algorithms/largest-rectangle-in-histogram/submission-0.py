class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = list()

        for i, height in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > height:
                index, poppedHeight = stack.pop()
                maxArea = max(maxArea, poppedHeight * (i - index))
                startIndex = index
            stack.append((startIndex, height))   

        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights) - i))     

        return maxArea    