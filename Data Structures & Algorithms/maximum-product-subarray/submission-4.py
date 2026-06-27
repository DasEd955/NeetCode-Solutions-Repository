class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float("-inf")
        curMin, curMax = 1, 1
        for num in nums:
            temp = num * curMax
            curMax = max(temp, num * curMin, num)
            curMin = min(temp, num * curMin, num)
            result = max(result, curMax)
        return result
