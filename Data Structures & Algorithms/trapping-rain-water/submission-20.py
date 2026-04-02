class Solution:
    def trap(self, height: List[int]) -> int:
        #max_area = 0

        #for i in range(len(height)):
            #max_left = max(height[:i+1] or [0])
            #max_right = max(height[i:] or [0])
            #trapped_water = min(max_left, max_right) - height[i]
            #max_area += trapped_water

        #return max_area  

        maxArea = 0
        left, right = 0, len(height) - 1
        maxLeft, maxRight = 0, 0

        if not height:
            return 0

        while left < right:
            if height[left] <= height[right]:
                maxLeft = max(maxLeft, height[left])
                maxArea += maxLeft - height[left]
                left += 1
            elif height[left] > height[right]:
                maxRight = max(maxRight, height[right])
                maxArea += maxRight - height[right]
                right -= 1
        return maxArea        



        