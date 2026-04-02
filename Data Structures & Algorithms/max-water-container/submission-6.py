class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0 
        left, right = 0, len(heights) - 1

        while left < right:
            currentArea = min(heights[left], heights[right]) * (right - left)
            if heights[left] <= heights[right]:
                if currentArea > maxArea:
                    maxArea = currentArea
                left += 1
            else:
                if currentArea > maxArea:
                    maxArea = currentArea
                right -= 1

        return maxArea                    
        