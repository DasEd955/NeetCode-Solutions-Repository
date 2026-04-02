class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0

        for i in range(len(height)):
            max_left = max(height[:i+1] or [0])
            max_right = max(height[i:] or [0])
            trapped_water = min(max_left, max_right) - height[i]
            max_area += trapped_water

        return max_area    



        