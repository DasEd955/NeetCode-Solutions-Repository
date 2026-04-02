class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)
        prefix, suffix = 1, 1

        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        for i in reversed(range(len(nums))):
            output[i] *= suffix
            suffix *= nums[i]

        return output        
        