class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k - 1)
    
    def atMost(self, nums: List[int], k: int) -> int:
        count, diff = dict(), 0 
        left, result = 0, 0

        for right in range(len(nums)):
            count[nums[right]] = 1 + count.get(nums[right], 0)
            if count[nums[right]] == 1:
                diff += 1
            while diff > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    diff -= 1
                left += 1
            result += (right - left + 1)
        
        return result