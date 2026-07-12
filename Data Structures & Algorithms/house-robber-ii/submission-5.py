class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] 

        cache1, cache2 = [-1] * len(nums), [-1] * len(nums)

        def dfs(i: int, partition: list[int], cache: list[int]) -> int:
            if i >= len(partition):
                return 0 
            if cache[i] != -1:
                return cache[i]
            take, skip = partition[i] + dfs(i + 2, partition, cache), dfs(i + 1, partition, cache)
            cache[i] = max(take, skip)
            return cache[i]

        return max(dfs(0, nums[0:-1], cache1), dfs(0, nums[1:], cache2))