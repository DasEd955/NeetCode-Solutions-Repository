class Solution:
    def trap(self, height: List[int]) -> int:

        maxArea = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = 0, 0

        while left < right:
            if height[left] <= height[right]:
                maxLeft = max(height[left], maxLeft)
                maxArea += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(height[right], maxRight)
                maxArea += maxRight - height[right]
                right -= 1

        return maxArea            
        