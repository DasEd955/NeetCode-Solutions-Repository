class Solution:
    def findMin(self, nums: List[int]) -> int:

        low, high = 0 , len(nums) - 1

        while low < high:
            middle = low + (high - low) // 2
            if nums[middle] <= nums[high]:
                high = middle
            else:
                low = middle + 1
        
        return nums[low]
        