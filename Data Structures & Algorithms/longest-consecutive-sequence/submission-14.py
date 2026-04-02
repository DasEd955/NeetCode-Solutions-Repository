class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
              
        if not nums:
            return 0

        sequence = list()
        nums.sort()
        print(nums)

        longest, currentCount = 0, 1

        for i in range(len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    currentCount += 1
                else:
                    longest = max(longest, currentCount)
                    currentCount = 1

        return max(longest, currentCount)                
                    