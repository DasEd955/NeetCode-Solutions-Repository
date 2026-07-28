class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = dict()

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num in nums:
            if count[num] > len(nums) / 2:
                return num
        