class Solution:
    def trap(self, height: List[int]) -> int:

        maxArea = 0
        maxLeft, maxRight = 0, 0
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] <= height[right]:
                maxLeft = max(maxLeft, height[left])
                maxArea += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                maxArea += maxRight - height[right]
                right -= 1

        return maxArea            
        