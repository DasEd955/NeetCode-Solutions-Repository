class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = 0
        left, right = 0, len(heights) - 1

        while left < right: 
            currentMax = min(heights[left], heights[right]) * (right - left)
            if heights[left] <= heights[right]:
                if currentMax > maxArea:
                    maxArea = currentMax
                left += 1
            else:
                if currentMax > maxArea:
                    maxArea = currentMax
                right -= 1

        return maxArea                    

        