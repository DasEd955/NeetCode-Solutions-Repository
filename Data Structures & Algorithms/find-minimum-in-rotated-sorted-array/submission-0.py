class Solution:
    def findMin(self, nums: List[int]) -> int:

        minimum = min(nums)
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == minimum:
                return nums[middle]
            elif nums[middle] < minimum:
                left = middle + 1
            else:
                right = middle - 1
        
        return min(nums)
        