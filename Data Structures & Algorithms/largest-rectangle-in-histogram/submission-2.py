class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0 
        length = len(heights)

        for i in range(length):

            height = heights[i]

            rightMost = i + 1
            while rightMost < length and heights[rightMost] >= height:
                rightMost += 1

            leftMost = i
            while leftMost >= 0 and heights[leftMost] >= height:
                leftMost -= 1

            leftMost += 1
            rightMost -= 1
            maxArea = max(maxArea, height * (rightMost - leftMost + 1))

        return maxArea        
        