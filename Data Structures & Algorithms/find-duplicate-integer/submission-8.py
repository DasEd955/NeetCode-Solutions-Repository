class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        low, high = 0, len(nums) - 1

        while low < high:
            middle = low + (high - low) // 2
            lessOrEqual = sum(1 for num in nums if num <= middle)
            if lessOrEqual > middle:
                high = middle
            else:
                low = middle + 1
        
        return low
        