class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()
        longest, currentCount = 0, 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    currentCount += 1
                else:
                    longest = max(longest, currentCount)
                    currentCount = 1

        return max(longest, currentCount)                                 
                    