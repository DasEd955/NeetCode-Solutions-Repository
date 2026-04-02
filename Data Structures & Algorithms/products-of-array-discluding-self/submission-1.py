class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = list()

        for index in range(len(nums)):
            output.append(math.prod(nums[:index]) * math.prod(nums[index+1:]))

        return output    
        