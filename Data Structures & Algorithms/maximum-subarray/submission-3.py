class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")

        for i in range(len(nums)):
            curSum = nums[i]
            result = max(result, curSum)
            for j in range(i + 1, len(nums)):
                curSum += nums[j]
                result = max(result, curSum)
        
        return result