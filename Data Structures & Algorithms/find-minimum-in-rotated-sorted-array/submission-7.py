class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2
            if nums[middle+1] < nums[middle]:
                return nums[middle+1]
            elif nums[middle-1] > nums[middle]:
                return nums[middle]
            elif nums[right] > nums[middle]:
                right = middle - 1
            elif nums[right] < nums[middle]:
                left = middle + 1  
        
        return nums[left]