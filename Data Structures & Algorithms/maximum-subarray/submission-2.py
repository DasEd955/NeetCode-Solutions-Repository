class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = list()

        for i in range(len(nums)):
            curSum = nums[i]
            result.append(curSum)
            for j in range(i + 1, len(nums)):
                curSum += nums[j]
                result.append(curSum)
        
        return max(result)