class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left, right = 0, len(heights) - 1
        #heights = sorted(heights)
        print(heights)

        max_area = (right - left) * min(heights[left], heights[right])
        while left < right:
            if heights[left] < heights[right]:
                left += 1
                current_max = (right - left) * min(heights[left], heights[right])
                if current_max > max_area:
                    max_area = current_max
                print(max_area)
            elif heights[left] >= heights[right]:
                right -= 1
                current_max = (right - left) * min(heights[left], heights[right])
                if current_max > max_area:
                    max_area = current_max
                print(max_area)
            #else:
                #print(current_max)
                #break
        
        return max_area        
                                 
        