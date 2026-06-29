from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = list()
        dp.append(nums[0])
        longest = 1
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                longest += 1
                continue
            index = bisect_left(dp, nums[i])
            dp[index] = nums[i]
        return longest