class Solution:
    def canJump(self, nums: List[int]) -> bool:

        i, farthest = 0, 0
        while i <= farthest and i <= len(nums):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                return True
            i += 1
        
        return False