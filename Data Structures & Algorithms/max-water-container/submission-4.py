class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            current_area = (right - left) * min(heights[left], heights[right])

            if heights[left] < heights[right]:
                left += 1
                if current_area > max_area:
                    max_area = current_area

            else:
                right -= 1
                if current_area > max_area:
                    max_area = current_area
        
        return max_area        
                                 
        