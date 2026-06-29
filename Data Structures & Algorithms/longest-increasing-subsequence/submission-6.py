class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = dict()
        for prev in range(-1, n):
            dp[(n, prev)] = 0
        for i in range(n - 1, -1, -1):
            for prev in range(-1, n):
                skip = dp[(i + 1, prev)]
                take = 0
                if prev == -1 or nums[i] > nums[prev]:
                    take = 1 + dp[(i + 1, i)]
                dp[(i, prev)] = max(take, skip)
        return dp[(0, -1)]