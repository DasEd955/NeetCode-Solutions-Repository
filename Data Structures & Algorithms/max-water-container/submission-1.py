class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left, right = 0, len(heights) - 1
        #heights = sorted(heights)
        print(heights)

        start_max = (right - left) * min(heights[left], heights[right])
        while left < right:
            if heights[left] < heights[right]:
                left += 1
                current_max = (right - left) * min(heights[left], heights[right])
                if current_max > start_max:
                    start_max = current_max
                print(start_max)
            elif heights[left] >= heights[right]:
                right -= 1
                current_max = (right - left) * min(heights[left], heights[right])
                if current_max > start_max:
                    start_max = current_max
                print(start_max)
            #else:
                #print(current_max)
                #break
        
        return start_max        
                                 
        