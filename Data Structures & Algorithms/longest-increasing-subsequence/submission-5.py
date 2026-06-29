class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        cache = dict()

        def dfs(i: int, prev: int) -> int:
            if i >= len(nums):
                return 0
            if (i, prev) in cache:
                return cache[(i, prev)]
            skip = dfs(i + 1, prev)
            take = 0
            if prev == float("-inf") or nums[i] > prev:
                take = 1 + dfs(i + 1, nums[i])
            choice = max(skip, take)
            cache[(i, prev)] = choice
            return choice
        
        return dfs(0, float("-inf"))