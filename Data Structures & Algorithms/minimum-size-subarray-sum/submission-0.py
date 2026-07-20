class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, shortest = 0, float("inf")
        windowSum = 0

        for right in range(len(nums)):
            windowSum += nums[right]
            while windowSum >= target:
                shortest = min(shortest, right - left + 1)
                windowSum -= nums[left]
                left += 1

        return shortest if shortest != float("inf") else 0