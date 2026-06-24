class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        curMin, curMax = 1, 1
        for num in nums:
            temp = curMax * num
            curMax = max(temp, curMin * num, num)
            curMin = min(temp, curMin * num, num)
            result = max(result, curMax)
        return result