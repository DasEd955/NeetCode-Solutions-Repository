class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False

        cache = dict()
        
        def dfs(i: int, target: int) -> bool:
            if i >= len(nums):
                return target == 0
            if target < 0:
                return False
            if (i, target) in cache:
                return cache[(i, target)]
            take = dfs(i + 1, target - nums[i])
            skip = dfs(i + 1, target)
            cache[(i, target)] = take or skip
            return cache[(i, target)]
        
        return dfs(0, sum(nums) // 2)