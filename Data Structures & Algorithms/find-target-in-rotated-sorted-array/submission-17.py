class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] >= nums[left]:
                if nums[middle] < target or nums[left] > target:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                if nums[middle] > target or nums[right] < target:
                    right = middle - 1
                else:
                    left = middle + 1
        
        return -1