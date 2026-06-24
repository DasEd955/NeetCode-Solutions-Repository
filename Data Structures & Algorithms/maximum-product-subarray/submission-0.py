class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = float("-inf")
        for start in range(len(nums)):
            product = 1
            for end in range(start, len(nums)):
                product *= nums[end]
                result = max(result, product)
        return result