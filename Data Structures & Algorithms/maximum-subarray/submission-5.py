class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        best = float("-inf")
        curSum = 0

        for i in range(len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            best = max(best, curSum)
        
        return best