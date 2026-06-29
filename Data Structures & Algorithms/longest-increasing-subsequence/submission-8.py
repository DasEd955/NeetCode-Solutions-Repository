class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        cache = [-1] * n

        def dfs(i: int) -> int:
            if cache[i] != -1:
                return cache[i]
            longest = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    longest = max(longest, 1 + dfs(j))
            cache[i] = longest
            return longest

        return max(dfs(i) for i in range(n))
        