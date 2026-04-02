class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        while left < right:
            current_max = (right - left) * min(heights[left], heights[right])

            if heights[left] < heights[right]:
                left += 1
                if current_max > max_area:
                    max_area = current_max

            else:
                right -= 1
                if current_max > max_area:
                    max_area = current_max
        
        return max_area        
                                 
        