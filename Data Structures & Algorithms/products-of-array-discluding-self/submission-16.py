class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefix, suffix = 1, 1

        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        for i in reversed(range(n)):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result