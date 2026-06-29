class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        
        for i in range(n - 1, -1, -1):
            longest = 1
            for j in range(n - 1, i, -1):
                if nums[i] < nums[j]:
                    longest = max(longest, 1 + dp[j])
            dp[i] = longest
        print(dp)
        return max(dp)