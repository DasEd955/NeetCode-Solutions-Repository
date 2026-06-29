class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2 != 0:
            return False
        
        n = len(nums)
        target = sum(nums) // 2
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[n][0] = True
        for i in range(n - 1, -1, -1):
            for s in range(target + 1):
                take = False
                if s >= nums[i]:
                    take = dp[i + 1][s - nums[i]]
                skip = dp[i + 1][s]
                dp[i][s] = take or skip
        return dp[0][target]