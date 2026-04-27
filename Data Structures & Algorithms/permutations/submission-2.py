class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        result = list()

        def dfs(nums: list[int], index: int) -> None:
            if index == len(nums):
                result.append(nums[:])
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                dfs(nums, index + 1)
                nums[index], nums[i] = nums[i], nums[index]
        
        dfs(nums, 0)
        return result
        